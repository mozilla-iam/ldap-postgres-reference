## User Profile
What we call the 'User profile' is a master profile for all users. It must contain all attributes fields that are in use by Mozilla LDAP and Mozillians.org.
The user profile is exposed to RPs (Relying Parties) in full or only partially, depending on a separate set of rules.
The CIS (Change Integration System) integrates all data sources into this user profile format.

### User_profile.json

This is the user profile we keep in CIS (Change Integration Service).

### User_profile_auth0_output.json

This is the user profile to be served by Auth0 when fed by CIS. It has additional values that are either required by Auth0, for backward compatibility, or required for OpenID Connect
But which are not part of the main user profile/CIS user profile. All new values are added dynamically by Auth0.

## SCIM
SCIM (System for Cross-Domain Identity Management) is a standard from https://www.simplecloud.info that is implemented by various tools.
The user schema or user profile part of SCIM is provided here as an example. The formal definition is hosted at http://www.simplecloud.info/specs/draft-scim-core-schema-01.html

## Auth0
Auth0 (https://www.auth0.com) contains an internal user schema that is sent via OIDC (OpenID Connect) through the ID Token and the user info endpoint.

## Workday
Workday is a SaaS (https://www.workday.com/) used by many companies to manager their work-force.
It can emit data about the work-force (such as who's an employee and their attributes) through a reporting system.

We provide a sample list of fields to be used by the CIS (Change Integration System) in other to integrate these into the user profile.
