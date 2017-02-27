#Reference architecture for Mozilla LDAP
from centos:7

#Patch CentOS
RUN yum update -y

#Install EPEL
RUN yum install epel-release -y

#Make life easier
RUN yum install vim -y

#Install ldap requirements
RUN yum install\
    openldap\
    openldap-servers\
    openldap-clients\
    nss_ldap\
    -y

#Install SQL back requirements
RUN yum install\
    openldap-servers-sql\
    unixODBC\
    -y

#Install the postgres client
RUN yum install\
    postgresql\
    postgresql-odbc\
    -y

#Setup the ODBC Connector
COPY ./odbc.ini /etc/odbc.ini

#Switch to /root
WORKDIR /root

#Copy in backsql_create
COPY ./backsql_create.sql /root/backsql_create.sql

#Copy in slapd config
COPY ./slapd.conf /etc/openldap/slapd.conf

#Clean the system
RUN yum clean all

#Setup openldap pid folder
RUN mkdir -p /usr/local/var

#Copy in entrypoint
COPY ./entrypoint.sh /root/entrypoint.sh

#Mark Entrypoint executable
RUN chmod u+rwx /root/entrypoint.sh

CMD ["/root/entrypoint.sh"]
