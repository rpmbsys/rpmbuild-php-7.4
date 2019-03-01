FROM aursu/rpmbuild:7-build

USER root

RUN yum -y --disablerepo=* --enablerepo=bintray-custom install \
        libzip \
    && yum clean all && rm -rf /var/cache/yum

RUN yum -y install --enablerepo custom \
        php-cli \
        php-common \
        php-devel \
        php-process \
        php-xml \
    && yum clean all && rm -rf /var/cache/yum