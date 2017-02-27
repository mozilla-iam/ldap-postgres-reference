#!/bin/bash

echo "Sleeping to allow postgres time to get ready. \n"
sleep 10

createdb -U postgres -h postgres pg_ldap
psql -U postgres -h postgres pg_ldap < backsql_create.sql
slapd -d 1 -f /etc/openldap/slapd.conf
