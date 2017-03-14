## User Profile
What we call the 'User profile' is a master profile for all users. It must contain all attributes fields that are in use by Mozilla LDAP and Mozillians.org.
The user profile is exposed to RPs (Relying Parties) in full or only partially, depending on a separate set of rules.
The CIS (Change Integration System) integrates all data sources into this user profile format.

## SCIM
SCIM (System for Cross-Domain Identity Management) is a standard from https://www.simplecloud.info that is implemented by various tools.
The user schema or user profile part of SCIM is provided here as an example. The formal definition is hosted at http://www.simplecloud.info/specs/draft-scim-core-schema-01.html

## Auth0
Autho (https://www.auth0.com) contains an internal user schema that is sent via OIDC (OpenID Connect) through the ID Token and the user info endpoint.

## Workday
Workday is a SaaS (https://www.workday.com/) used by many companies to manager their work-force.
It can emit data about the work-force (such as who's an employee and their attributes) through a reporting system.

We provide a sample list of fields to be used by the CIS (Change Integration System) in other to integrate these into the user profile.
