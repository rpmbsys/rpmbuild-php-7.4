# remirepo/fedora spec file for argon2
#
# Copyright (c) 2017 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global libname      libargon2
%global gh_commit    1c4fc41f81f358283755eea88d4ecd05e43b7fd3
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     P-H-C
%global gh_project   phc-winner-argon2
%global soname       0

%global upstream_version 20161029
#global upstream_prever  RC1

Name:    argon2
Version: %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release: 2%{?dist}
Group:   Applications/System
Summary: The password-hashing tools

License: Public Domain or ASL 2.0
URL:     https://github.com/%{gh_owner}/%{gh_project}
Source0: https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{upstream_version}%{?upstream_prever}-%{gh_short}.tar.gz
BuildRequires: gcc

Requires: %{libname}%{?_isa} = %{version}-%{release}


%description
Argon2 is a password-hashing function that summarizes the state of the art
in the design of memory-hard functions and can be used to hash passwords
for credential storage, key derivation, or other applications.

It has a simple design aimed at the highest memory filling rate and
effective use of multiple computing units, while still providing defense
against tradeoff attacks (by exploiting the cache and memory organization
of the recent processors).

Argon2 has three variants: Argon2i, Argon2d, and Argon2id.

* Argon2d is faster and uses data-depending memory access, which makes it
  highly resistant against GPU cracking attacks and suitable for applications
  with no threats from side-channel timing attacks (eg. cryptocurrencies). 
* Argon2i instead uses data-independent memory access, which is preferred for
  password hashing and password-based key derivation, but it is slower as it
  makes more passes over the memory to protect from tradeoff attacks.
* Argon2id is a hybrid of Argon2i and Argon2d, using a combination of
  data-depending and data-independent memory accesses, which gives some of
  Argon2i's resistance to side-channel cache timing attacks and much of
  Argon2d's resistance to GPU cracking attacks.


%package -n %{libname}
Group:    System Environment/Libraries
Summary:  The password-hashing library

%description -n %{libname}
Argon2 is a password-hashing function that summarizes the state of the art
in the design of memory-hard functions and can be used to hash passwords
for credential storage, key derivation, or other applications.


%package -n %{libname}-devel
Group:    Development/Libraries
Summary:  Development files for %{libname}
Requires: %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname}-devel
The %{libname}-devel package contains libraries and header files for
developing applications that use %{libname}.


%prep
%setup -qn %{gh_project}-%{gh_commit}

if ! grep -q 'soname,%{libname}.so.%{soname}' Makefile; then
  : soname have changed
  grep soname Makefile
  exit 1
fi

# Fix pkgconfig file
sed -e 's:lib/@HOST_MULTIARCH@:%{_lib}:;s/@UPSTREAM_VER@/%{version}/' -i %{libname}.pc

# Honours default RPM build options and library path, do not use -march=native
sed -e 's:-O3 -Wall:%{optflags}:' \
    -e '/^LIBRARY_REL/s:lib:%{_lib}:' \
    -e 's:-march=\$(OPTTARGET) :${CFLAGS} :' \
    -e 's:CFLAGS += -march=\$(OPTTARGET)::' \
    -i Makefile

%build
# parallel build is not supported
make -j1


%install
make install DESTDIR=%{buildroot}

# Drop static library
rm %{buildroot}%{_libdir}/%{libname}.a

# Create link to soname, see Makefile for value
mv %{buildroot}%{_libdir}/%{libname}.so %{buildroot}%{_libdir}/%{libname}.so.%{soname}
ln -s %{libname}.so.%{soname} %{buildroot}%{_libdir}/%{libname}.so

# pkgconfig file
install -Dpm 644 %{libname}.pc %{buildroot}%{_libdir}/pkgconfig/%{libname}.pc

# Fix perms
chmod -x %{buildroot}%{_includedir}/%{name}.h


%check
make test


%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files
%{_bindir}/%{name}

%files -n %{libname}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%{_libdir}/%{libname}.so.%{soname}

%files -n %{libname}-devel
%doc *md
%{_includedir}/%{name}.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc


%changelog
* Thu Nov 16 2017 Milan Broz <gmazyland@gmail.com> - 20161029-2
- Do not use -march=native in build, use system flags (rh #1512845).

* Wed Oct 18 2017 Remi Collet <remi@remirepo.net> - 20161029-1
- initial package
