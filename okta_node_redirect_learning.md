#  Learning how to integrate Okta with a local web app (nmp)

## Overview
Two parts to this learning
- Part 1: use an already-created sample app, via a tool that installs and configures that app
- Part 2 do it manually, and understand it

## Part 1

Using an already created sample app....

Follow instructions here https://github.com/okta-samples/okta-express-sample/tree/main

* Install Okta CLI https://github.com/okta/okta-cli#installation
 - run curl https://raw.githubusercontent.com/okta/okta-cli/master/cli/src/main/scripts/install.sh | bash
   - throws an error related to funzip
     - so, run sudo apt install unzip
   - run that curl command piped to bash, again
 - close and reopen terminal.  Run okta --version to confirm installation

- Run through commands here: https://github.com/okta-samples/okta-express-sample/tree/main?tab=readme-ov-file
 - run okta start express
   - follow prompts to create a developer account - assuming don't have one
   - cd to express directory (it was created when ran okta start express(?)), then run nmp install
   - Note: npm install installs the packages into the node_modules folder in the express project folder that the okta start express command created...this is a node project folder (?)...one can have multiple - each with their own local dependencies(?)

## Part 2

Understand things, and do them manually
- Read through the stuff that helps with understanding this all better
  - https://developer.okta.com/docs/concepts/
  - https://developer.okta.com/docs/concepts/redirect-vs-embedded/

- Do the manual steps https://developer.okta.com/docs/guides/sign-into-web-app-redirect/node-express/main/

### Learning/reading notes

Looks like redirect (vs embedded) (vs embedded sdk driven sign in) is the typical/preffered approach...(? https://developer.okta.com/docs/concepts/redirect-vs-embedded/)
- Redirect...redirects the user to Okta (to the Okta widget...hosted by (?) Okta).  
- Embedded widget - you are getting it from CDN, or NPM, etc. you host and manage own version (?) and manage https://developer.okta.com/docs/guides/embedded-siw/main/
- In any case where you use the widget, your code/app has logic in it to call the widget (?)  ... in the embedded case, your app hosts the widget and you customize it
- Embded sdk driven ... doesn't use the widget at all (?).  Your code does all the authentication stuff/session management stuff (?)...just uses the Okta API for authing the user?


### Manual steps notes

	Callback URL (also known as the redirect URL) - where Okta sends the cleient after authentication. Its usually a page that handles whatever information (assertions or claims (?) it gets back from Okta, and sets up a user session, and then, potentially, redirects them again to a landing page, or perhaps the page 
	- Note: this URL can be overridden by a redirect URL that the webpage sending the authentication request to Okta specifies (in case, for instance, the user should be redirected to whatever page they were trying to access in the first place)



