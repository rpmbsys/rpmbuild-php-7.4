FROM aursu/rpmbuild:7-build

USER root

RUN yum -y --enablerepo=custom --enablerepo=bintray-custom install \
        php-cli \
        php-common \
        php-devel \
        php-process \
        php-xml \
    && yum clean all && rm -rf /var/cache/yum