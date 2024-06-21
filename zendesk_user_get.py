import requests
import json

from requests.auth import HTTPBasicAuth


user_to_query_for_email = "sachs.davidr@gmail.com"
zendesk_api_drs_url = f'https://davidrobertsachs.zendesk.com/api/v2/search.json?query=email:{user_to_query_for_email}'
zendesk_api_user_email = "sachs.davidr@gmail.com"
zendesk_api_token = "BQBQEzzCdEIwtijCwGR7E2gvpSAli9ahNY7PXsPk"

response = requests.get(zendesk_api_drs_url, auth=HTTPBasicAuth(zendesk_api_user_email + '/token', zendesk_api_token))

json.loads(response.text)

# to pretty print: print(json.dumps((json.loads(response.text)), indent=4))