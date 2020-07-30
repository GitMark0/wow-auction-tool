import requests
from requests.auth import HTTPBasicAuth


def retrieve_token(client_id, client_secret, region='eu'):
    url = f'https://{region}.battle.net/oauth/token'
    body = {'grant_type': 'client_credentials'}
    auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.post(url, data=body, auth=auth)
    return response.json()


def make_request(url):
    base_url = 'https://eu.api.blizzard.com/data/wow/connected-realm/'
    response = requests.get(base_url + url)
    return response.json()


CLIENT_ID = '4765849c9d3a4ae7a1132515105cba14'
CLIENT_SECRET = 'WZrsyckvjFLXVyNxEnGKCuS3is8I5Spw'

# token_info is a dictionary with k, v pairs:
# "access_token": "USVb1nGO9kwQlhNRRnI4iWVy2UV5j7M6h7",
# "token_type": "bearer",
# "expires_in": 86399,
# "scope": "example.scope"

token_info = retrieve_token(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET)

access_token = token_info['access_token']

# Retrieve ID's of available EU servers
connected_realm_IDs = make_request(
    f'index?namespace=dynamic-eu&locale=en_GB&access_token={access_token}')

server_id = 1302  # Archimonde EU server ID

# Retrieve info for specific server ID
connected_realm_info = make_request(
    f'{server_id}?namespace=dynamic-eu&locale=en_GB&access_token={access_token}')

# Archimonde server AH data
ah_data = make_request(
    f'{server_id}/auctions?namespace=dynamic-eu&locale=en_GB&access_token={access_token}')
print('Hello')
