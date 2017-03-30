"""User factory for faking user profiles."""
from faker import Factory
import pprint

class User(object):
    """Returns a fake user using the faker lib."""
    def __init__(self):
        self.fake = Factory.create()
        self.name = self.fake.name()
        self.profile = self.fake.profile(fields=None, sex=None)

    def user_id(self):
        """Returns single attribute of user_id."""
        return self.profile['username']

    def timezone(self):
        """Returns single attribute of tz."""
        return self.fake.timezone()

    def lastModified(self):
        """Returns current ts in zulu time."""
        return self.fake.date_time(tzinfo=None)

    def created(self):
        """Returns ts in zulu time."""
        return self.fake.date_time(tzinfo=None)

    def username(self):
        """Returns random username."""
        return self.profile['username']

    def displayName(self):
        return self.profile['name']

    def firstName(self):
        return self.profile['name'].split(' ')[0]

    def lastName(self):
        return self.profile['name'].split(' ')[1]

    def preferredLanguage(self):
        return self.fake.language_code()

    def primaryEmail(self):
        return self.profile['mail']

    def emails(self):
        """emails": [
            {
                "value": "jdoe@mozilla.com",
                "verified": true,
                "primary": true,
                "name": "work"
            },
        """
        mails = []
        for _ in range(0, 4):
            mails.append(
                {
                    "value": self.fake.email(),
                    "verified": 'true',
                    "primary": 'false',
                    "name": "random"
                }
            )
        mails.append(
            {
                "value": self.profile['mail'],
                "verified": 'true',
                "primary": 'true',
                "name": "work"
            }
        )
        return mails

    def phoneNumbers(self):
        """
        "phoneNumbers": [
            {
                "value": "+33169288888",
                "verified": false,
                "name": "My French mobile phone"
            },
        """
        phones = []
        for _ in range(0, 6):
            phones.append(
                {
                    "value": self.fake.phone_number(),
                    "verified": 'true',
                    "name": "A random phone"
                }
            )
        return phones


    def uris(self):
        """
        "uris": [
                {
                    "value": "https://www.insecure.ws",
                    "primary": true,
                    "verified": false,
                    "name": "Blog"
                },
        """
        uris = []
        for _ in range(0, 7):
            uris.append(
                {
                    "value": self.fake.url(),
                    "primary": 'true',
                    "verified": 'false',
                    "name": "A website"
                }
            )
        return uris


    def nicknames(self):
        """
        "nicknames": [
            {
                "value": "jdoe",
                "primary": true,
                "verified": false,
                "name": "Mozilla IRC"
            }
        ],
        """
        return []

    def SSHFingerprints(self):
        """
        "SSHFingerprints": [
                {
                    "value": "4096 SHA256:rlhYcDi2e98sekBwu9aaPEmr3xsg1CsS1tGXksSTSIg test (RSA)",
                    "primary": true,
                    "verified": false,
                    "name": "Mozilla SSH"
                }
            ],

        """
        return []

    def PGPFingerprints(self):
        """
        "PGPFingerprints": [
                {
                    "value": "0x61AB87D6F66CE2FCD2D2E1F56A65DFA844722517",
                    "primary": true,
                    "verified": false,
                    "name": "Mozilla PGP"
                }
            ],
        """
        return []

    def picture(self):
        return self.fake.image_url()

    def shirtSize(self):
        return "xs"

    def membership(self):
        """Return list of dicts.
            "Mozillian.org": [
                {
                    "created": "2010-01-23T04:56:22Z",
                    "lastUsed": "2010-01-23T04:56:22Z",
                    "name": "IAM",
                    "uuid": "xxxx1",
                    "roles": [ "user" ]
                    },
        """
        return {
            "Workday": [{
                "created": "2010-01-23T04:56:22Z",
                "lastUsed": "2010-01-23T04:56:22Z",
                "name": "IAM",
                "uuid": "xxxx1",
                "roles": ["user"]
            }],
            "LDAP": [{
                "created": "2010-01-23T04:56:22Z",
                "lastUsed": "2010-01-23T04:56:22Z",
                "name": "IAM",
                "uuid": "xxxx1",
                "roles": ["user"]
            }],
            "Mozillianorg": [{
                "created": "2010-01-23T04:56:22Z",
                "lastUsed": "2010-01-23T04:56:22Z",
                "name": "IAM",
                "uuid": "xxxx1",
                "roles": ["user"]
            }],
        }


    def enriched_profile(self):
        return {
                "app_metadata": {
                    "invalid": "invalid bug work around"
                },
                "timezone": self.timezone(),
                "username": self.primaryEmail(),
                "displayName": self.displayName(),
                "lastModified": self.lastModified(),
                "created": self.created(),
                "firstName": self.firstName(),
                "lastName": self.lastName(),
                "preferredLanguage": self.preferredLanguage(),
                "primaryEmail": self.primaryEmail(),
                "emails": self.emails(),
                "phoneNumbers": self.phoneNumbers(),
                "uris": self.uris(),
                "nicknames": self.nicknames(),
                "SSHFingerprints": self.SSHFingerprints(),
                "PGPFingerprints": self.PGPFingerprints(),
                "picture": self.picture(),
                "shirtSize": self.shirtSize(),
                "membership": self.membership(),
                "active": 'true'
            }

if __name__ == "__main__":
    u = User()
    #print(pprint.pprint(u.profile))
    print(pprint.pprint(u.enriched_profile()))
