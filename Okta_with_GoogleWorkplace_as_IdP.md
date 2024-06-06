Excercise: Start Google Workspace trial and Okta trial, and set up Google as IdP for Okta (and apps behind Okta(?))

Preread...Identity provider learning: https://help.okta.com/en-us/content/topics/security/identity_providers.htm

Steps:
Google side: https://support.google.com/a/answer/6087519?sjid=6078672521519177148-NC

Google side specifics:
- Name the app "Okta as Service Provider"
- Name ID format: Unspecified (not sure if this is is the only viable option)
- Name ID: Basic Information > Primary Email
- SAML Attribute Mappings:
- Primary email: email
- First name: firstName
- Last name: lastName

Okta side: https://help.okta.com/en-us/content/topics/security/idp-add-saml.htm

Okta side Specifics:
- Name: "Google Workspace IDP"
- IdP username: idpuser.subjectNameId (not sure why)
- Account Link Policy: Automatic
- If no match found: Creatr new user (JIT)
- Update attributes for existing users: true (not sure if this is actually needed)