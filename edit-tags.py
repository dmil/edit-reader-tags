import json
import requests

BASE_URL = "https://readwise.io/api/v2/auth/"
with open("keys.json") as keys_file:
    keys = json.load(keys_file)
    token = keys["access_token"]

def test_auth():
    url = BASE_URL
    headers = {"Authorization": "Token " + token}
    response = requests.get(url, headers=headers)
    assert(response.status_code == 204)

test_auth()


