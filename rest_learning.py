# https://docs.python-requests.org/en/latest/user/quickstart/
# python -m pip install requests
import requests
r = requests.get('https://api.github.com/events')


r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')
r = requests.head('https://httpbin.org/get')
r = requests.options('https://httpbin.org/get')

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
r.text
r.encoding
r.content
r.encoding = 'ISO-8859-1'
r.text
r.json()
r.status_code
r.headers['Server']
r.headers['Content-Type']
r.cookies
r.history

# Timeouts
# You can tell Requests to stop waiting for a response after a given number of seconds with the timeout parameter.
# Nearly all production code should use this parameter in nearly all requests. Failure to do so can cause your program
# to hang indefinitely...

requests.get('https://github.com/', timeout=0.1)
