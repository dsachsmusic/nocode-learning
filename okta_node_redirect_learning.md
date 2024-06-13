#  Learning how to integrate Okta with a local web app (nmp)

h2. Overview
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
   - follow prompts to create a developer account - assuming don't have one)
   - cd to express directory (it was created when ran okta start express(?)), then run nmp install
   - Note: npm install installs the packages into the node_modules folder in the express project folder that the okta start express command created...this is a node project folder (?)...one can have multiple - each with their own local dependencies(?))

## Part 2

Understand things, and do them manually
- Read through the stuff that helps with understanding this all better
  - https://developer.okta.com/docs/concepts/
  - https://developer.okta.com/docs/concepts/redirect-vs-embedded/

- Do the manual steps https://developer.okta.com/docs/guides/sign-into-web-app-redirect/node-express/main/
