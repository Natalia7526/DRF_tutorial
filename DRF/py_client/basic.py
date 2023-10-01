import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "https://httpbin.org/sttus/200/"

# get_response = requests.get(endpoint)  # HTTP Request
get_response = requests.get(endpoint, json={"query": "Hello world"})  # HTTP Request with added dictionary
print(get_response.text)  # print raw text response

# API [Application Programming Interface] -> Method
# Phone -> Camera -> App -> API -> CAMERA
# HTML Request -> HTML
# REST API request (http) -> JSON (xml)
# JavaScript Object Notation ~ Python Dictionary (only almost like python dictionary but is something different)

print(get_response.json())

# example for get_response = requests.get(endpoint)
# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', '
# Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-
# requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-651955a8-30cf922a71074d66044a9885'}
# , 'json': None, 'method': 'GET', 'origin': '188.122.20.102', 'url': 'https://htt
# pbin.org/anything'}

# example for get_response = requests.get(endpoint, json={"query": "Hello world"})
# {'args': {}, 'data': '{"query": "Hello world"}', 'files': {}, 'form': {}, 'heade
# rs': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '24
# ', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'pyt
# hon-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-6519563f-383bb27e0f606c401462ea
# f4'}, 'json': {'query': 'Hello world'}, 'method': 'GET', 'origin': '188.122.20.1
# 02', 'url': 'https://httpbin.org/anything'}
