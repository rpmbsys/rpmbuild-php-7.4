ARG centos=7.9.2009
ARG image=devbase
FROM aursu/php74build:${centos}-${image}

RUN curl -sSL https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
