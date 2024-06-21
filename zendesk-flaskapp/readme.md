# Overview
Flask webpage interacting with Zendesk (and possibly other tools(?)

# Setup
Set up channel for messaging: Zendesk > Admin Center > Channels > Messaging > Add Channel > Web Widget (?)
  - Copy the script/save it somewhere
  
Get API token: Zendesk > Admin Center > Integrations > Zendesk API > Add API token
  - Copy the token - save it somewhere safe (note: in production, this token should never be saved or made visible in plain text
  
Have Flask set up on ... details on set up not convered here. And have requirements installed (also not covered here)

# Learning notes and concepts
## Flask app that gets some info back from an api in response to text from a form (and, somewhat unrelated: on the peripheral, includes a chat widget)
### Making Basic Auth API call using Python
- Zendesk API call for searching for a user by email address: https://davidrobertsachs.zendesk.com/api/v2/search.json?query=email:<username>'
- Basic Auth with Python: (method we are using is Basic Auth - we have this configured to be allowed in our Zendesk trial)
  - The Python requests library has a module (?) called HTTPBasic Auth - we import it (from requests.auth import HTTPBasicAuth), and then, use it as a parameter in our request.get() call...
    -  auth=HTTPBasicAuth(username, token)
- In Zendesk, the username field, for Basic Auth is "emailaddress/token" (? apparently), so we write our request.get() call as:
  - requests.get(zendesk_api_url, auth=HTTPBasicAuth(zendesk_api_user_email + '/token', zendesk_api_token))

### Creating a form to interact with, that makes API call
- To make a form that a user can fill out, and submit, and, get some sort of info back based on results from an api call...
  - Form - an HTML element (?)...with a "method" property (?)...example < form method="post">, and label and input tags...
    - ...Input labels...which we configure with properties like "type", and values for "type" such as "text" (for the text field), or "submit" for a submit button
	- Altogether, we have a form that a user can fill out, and it sends a "post" (or whatever method)
- Note: for were to put this HTML element...see "Putting Flask and HTML together..."

### Flask app config details
- Flask app should be configured to respond to both "get" and "post"...
  - For example: @app.route('/', methods=['GET', 'POST'])
  - This is because we are making a single webpage that 1) loads when somebody navigates to it, and 2) responds to post method that a form creates
- Flask app function definition includes a condition for if the request type is "POST", make an API call, and, process the results, and return some related text 
  - ie - Flask app loads the page for a GET call (i.e. if somebody types the URL into a browser), and then, if somebody fills out the form, and clicks submit, the form, sends a POST request...and in response, said Flask condition is triggered 	
  - Specific logic for if POST condition is met below, in "Putting Flask and HTML together..."
  
### Putting Flask and HTML together using Jinja2 template 	
- Note: this all might have been able to been coded into the Flask app, perhaps...using Javascript and HTML (?), but, templates are good...we are doing MVC 
- In Flask app directory, create a templates folder, and create a file (index.html, for example), with HTML file (head, body, etc), include HTML form element, in body 
- Note: Reminder...In Flask w/Jinja2 templating, we can have server side script variables and flow determine if a template, is "rendered"(?) i.e. if html is loaded, and with what specific values (from given variables)
- Create server side logic to render the HTML template as a view (MVC)/webpage, in response to a GET call
  - return render_template('index.html')
- Create server side logic in the Flask app for making an API call if request is a POST...using the text from the post as values in an API call, and, collecting the results of the API into a variable named "message"
  - return render_template('index.html', message=message)
- Insert, into index.html, Jinja templating language for creates and populating an HTML element (<p> element, for example), if a variable "message" is not null
  - {% if message %} <p>{{ message }}</p> {% endif %} (note: not sure if this requeires carriage returns and indentation)

### Including the Messaging widget
- Paste that Web Widget script copied earlier into the HTML body. 
	