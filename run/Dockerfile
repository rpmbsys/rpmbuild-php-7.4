ARG image=7-web
FROM aursu/centos:${image}

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

ENV PHP_FPM_PM_STYLE dynamic
ENV PHP_FPM_PM_MAX_CHILDREN 800
ENV PHP_FPM_PM_START_SERVERS 5
ENV PHP_FPM_PM_MIN_SPARE_SERVERS 5
ENV PHP_FPM_PM_MAX_SPARE_SERVERS 35
ENV PHP_FPM_PM_MAX_REQUESTS 500

WORKDIR /var/www/html
EXPOSE 9000
CMD [ "/usr/sbin/php-fpm", "--nodaemonize" ]
