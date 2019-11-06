ARG centos=7
FROM aursu/rpmbuild:${centos}-build

USER root

COPY system/etc/yum.repos.d/bintray-custom.repo /etc/yum.repos.d/bintray-custom.repo

RUN yum -y --enablerepo=custom --enablerepo=bintray-custom --enablerepo=bintray-php73custom install \
        php-cli \
        php-common \
        php-devel \
        php-process \
        php-xml \
    && yum clean all && rm -rf /var/cache/yum