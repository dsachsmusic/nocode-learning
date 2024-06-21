from flask import Flask, render_template, request
import requests
import json
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

# Configuration for Zendesk API
zendesk_api_user_email = "sachs.davidr@gmail.com"
zendesk_api_token = "BQBQEzzCdEIwtijCwGR7E2gvpSAli9ahNY7PXsPk"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get username from the form
        username = request.form['username']

        # Construct Zendesk API URL
        zendesk_api_url = f'https://davidrobertsachs.zendesk.com/api/v2/search.json?query=email:{username}'

        # Make API request to Zendesk
        response = requests.get(zendesk_api_url, auth=HTTPBasicAuth(zendesk_api_user_email + '/token', zendesk_api_token))

        if response.status_code == 200:
            # Parse JSON response
            data = json.loads(response.text)

            if 'results' in data and len(data['results']) > 0:
                # Extract information from the response
                user_name = data['results'][0]['name']
                message = f"We've found your record: {user_name}!"
            else:
                message = "User not found in Zendesk."

            return render_template('index.html', message=message)

    # If it's a GET request or username not found, render the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='10.0.0.4', port=8080, debug=True)