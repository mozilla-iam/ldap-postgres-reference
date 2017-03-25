# User stories for CIS and User profile

These are lightweight user stories we though of for users of the CIS (Change Integration Service) and the user profile.

## Roles

* CIS Writer: Person in charge of a system sending user profile updates to the CIS (mozillians.org, work day, etc.)
* Auth0 Reader: RP (Relying Party) getting user profile data from Auth0 (mozillians.org, discourse, airmo, Gmail, etc.)
* Account manager: Person in charge of setting access control

## User stories

CIS Writers:
* I want to be be notified if the profile update failed
* I want CIS to be the only mechanism updating the user profile
* I want to send complete user profiles when updating, instead of deltas/diffs
* I want *some* of the user profile information to be marked as private/only accessible by some RPs
* I want to be able to send *any* profile update without modifying my code, and CIS to figure things out and integrate the data correctly

Auth0 Reader:
* I want all information from auth0 to reflect the current state of a user profile, at all times (including when writes/updates to the profile failed)
* I want to know if a user has access to my service without creating custom groups or relying on uncertain group data
* I want to get as much information about the user as possible/allowed
* I want to be able to tell which is the primary email address for the user
* I want to be able to tell what other accounts, emails, etc the user has. For example, what's his user account on GitHub?
* I want the user profile to be stable enough so that field names do not change or disappear unexpectedly (or ever)

Account manager:
* I want to be able to say which services (RP) a user has access to
* I want to be able to say which users a service (RP) gives access to
* I want to be able to set access based on LDAP groups, Workday attributes, Mozillians.org groups or service (RP)
