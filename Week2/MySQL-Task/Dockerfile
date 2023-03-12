FROM ubuntu:18.04
RUN apt-get update

#Add an account for running MySQL
RUN groupadd -r mysql && useradd -r -g mysql mysql

#Install MySQL
RUN apt-get install -y mysql-server \
    && mkdir -p /var/lib/mysql /var/run/mysqld \
    && chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \
    && chmod 777 /var/run/mysqld

# Make sure my.cnf file is in the same dir as Dockerfile
COPY ./my.cnf /etc/mysql/conf.d

EXPOSE 3306

# Start mysql
CMD ["mysqld","--user","mysql"]