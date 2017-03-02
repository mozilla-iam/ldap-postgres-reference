# Mozilla LDAP Reference Implementation


## Purpose

The purpose of this project is to become a reference implementation for development against during the Identity and Access Management Project.

## Progress

* Initial Build of SQL Backed LDAP Based on CentOS 7.3 : Complete __2/27/2017__
* Tested against Postgres 9.4 : Complete __2/27/2017__
* Integration with Kafka Job Server for Modifications _not started_
* Move database init to postgres container
* Ansible Container for Customization _started_ ( mostly ready for test ... )
* Security Unit Test _not started_
* Automatic generation and output TLS Certs _not started_

## Getting started

1. Touch a virtual environment in the directory for python. `virtualenv .`
2. Activate the virtualenv `source bin/activate`
3. Install ansible-container `pip install -r ansible/requirements.txt`
4. Update the vars in `ansible/main.yml` and `ansible/container.yml` with your desired passwords.  These will be used to setup the templates for use with ldap+postgres.
5. Build the containers from the top level directory `ansible-container build`
6. Run the project very much like you would run with compose.  `ansible-container run`
