FROM node:20.17.0-slim AS web

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

RUN npm run build

FROM php:8.2-apache

ENV MAKEFLAGS=-j4

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y libzip-dev zip && \
    docker-php-ext-install zip && \
    pecl install grpc && \
    docker-php-ext-enable grpc

RUN a2enmod rewrite

WORKDIR /var/www/html

ENV APACHE_DOCUMENT_ROOT=/var/www/html/public
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf

COPY --from=web /app .
# COPY .env .

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN composer install

RUN chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache /var/www/html/database
