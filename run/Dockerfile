FROM aursu/centos:7-web

COPY system/etc/yum.repos.d/bintray-custom.repo /etc/yum.repos.d/bintray-custom.repo

RUN yum -y --enablerepo=bintray-custom --enablerepo=bintray-php73custom install \
        php-bcmath \
        php-cli \
        php-fpm \
        php-opcache \
        php-pecl-apcu \
        php-pecl-geoip \
        php-pecl-imagick \
        php-pecl-memcached \
        php-pecl-redis4 \
        php-sodium \
        php-xml \
    && yum clean all && rm -rf /var/cache/yum

# php-fpm configuration
COPY system/etc/php-fpm.conf /etc/php-fpm.conf
COPY system/etc/php-fpm.d/www.conf /etc/php-fpm.d/www.conf

WORKDIR /var/www/html
EXPOSE 9000
CMD [ "/usr/sbin/php-fpm", "--nodaemonize" ]
