# Tangent: talking to ChatGPT to understand Oauth/OIDC and SAML better
- Service provider sends authentication request to identity provider, identity provider authenticates user, and then, sends an assertion (SAML assertion), or Ouath token, JWT, with claims ("claims" is more or less synonymous with "assertions")
  - Sends the assertion/token through the client?  i.e. client, such as web browser, takes the assertion/token and hands it to the service provider?
  - Assertions/claims include attributes (user ID, group membership, etc)
- More about assertions and tokens
  - assertions...
    - ?
  - tokens
    - Oauth tokens and OIDC tokens...
	  - Oauth tokens are for authentication, OIDC tokens are used for authorization (claims, etc).
	    - Sometimes Oauth tokens are used for authorization (?), for example, bearer tokens (?)
	  - In SAML, you just have the assertion (?) it includes both authentication and authorization info?
    - Oauth tokens...can be JWT format, or other formats
      - note: JWT is not soley related to Oauth...(?)
      - other formats include, random string, opaque, and reference tokens...
	  - different types of tokens have different (?) (sometimes overlapping (?)) uses
	  - JWTs, used as Oauth tokens, are, especially useful (?); include, header payload, and signature, for easy parsing (?)
	  - A specific type of Oauth token, called bearer token, is JWT format
	- OIDC tokens...
	  - are always JWT?
    - JWTs...a bit of info on them
      - URL-safe (doesn't require encoding...does not use characters not allowed in a URL)
	- include header, payload, and signature 
	- claims...in tokens 
	  - ? provide information about the user's identity, attributes, and other relevant data.
	- access tokens and refresh tokens
	  - access tokens short lived...following access token, get and use refresh tokens to maintain authentication
- Authorization
  - the service provider uses information from the claim to decide what access to grant to resources
    - in Oauth, there is a term called "resource server" and the idea of "resources" ... it is a general concept...the idea that, on the service provider side, there are resources that can be granted access to (?)
- More on Oauth
  - ?
- More on SAML
  - uses XML
  - Flow types: authorization Code Flow, Implicit Flow, Client Credentials Flow, etc.


# Bonus: other learning notes
## some SAML and Oauth notes from a youtube video
Identity Provider
Service Provider

SAML
- SAML request
- SAML Response
- Assertion Consumer Service URL
- Callback URL (?)

Oauth/OIDC:
- Oauth for authorization, OIDC for authentication (?)
- Oauth is a framework, not a spec (or whatever)...it leaves many elements open to interpretation/growth (and development of extensions)
  - Extensions like
    - OIDC
    - some delegation...concept, useful for microservices, where auth info needs to be sent/passed off between services?

## some OAuth/OIDC notes from a training
OIDC - really good for bootstapping user acccounts ...what is used when you use a social media app log in...as your log in for something - the OIDC ...thing...whatever its called, sends that info (can send a bunch of info) that, that the resource server/service provider/whatever can then use to bootstap a user account for the user
Grants - what are they?
Scopes - what are they?
In OIDC, there is something called an ID token...and that is always a JWT
JWTs, btw, include header, payload, and signature
- header includes an algorithm, with which the payload (whatever important data...) gets encrypted, and signature - to prove hasn't been tampered with, perhaps (if they share a trusted root) sender is who says it is

Resource Server, Resource Owner (what is a resource owner)

In Oauth, there is...
- Authorization server and token server ... can be the same, but, there are use cases for it to be sifferent...so, two separate things in spec
  - like, the auth code flow?  where user gets an auth code...and then server does something ... (?)
- Client type?  Device (API to API, for example?) ?  Or User/browser?  
- and, given combination of these things/scenarios, there are different flows?

Flows - different flows work/offer security/are feasible for different scenarios
- Devices without browsers
- single page apps (store everything client side - which can be an issue)
- etc.
- problems are where to put any secret information/log in information?
- issue of potential of token being taken...in the browser?  by another application running in the browser?
- most popular/best Oauth flow is the Authorization Code Flow 
  - User gets auth code...
  - Exchanges it for a token, or something?
  - application (server?  or something) gets...a token?  
  - idk

Information in token includes...
- sub (subject name?)
- iat - issured at time
- exp - expiration
- etc.
- etc (?)
- How long token is set to last...depends on security...if its youtube...maybe let token last longer...if it is banking ...
