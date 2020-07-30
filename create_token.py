import requests
from requests.auth import HTTPBasicAuth
import re


def get_ah_data(server_id, access_token):
    # Request for AH data of specific server_id
    ah_data = make_request(
        f'{server_id}/auctions?namespace=dynamic-eu&locale=en_GB&access_token={access_token}')
    return ah_data


def get_connected_realm_ids(access_token):
    # Retrieve ID's of available EU servers
    connected_realm_index = make_request(
        f'index?namespace=dynamic-eu&locale=en_GB&access_token={access_token}')

    # Extract all connected realm ID's from realm indexes.
    connected_realm_IDs = list()
    for entry in connected_realm_index['connected_realms']:
        link = entry['href']
        id = re.findall(r'\d+', link)[0]
        connected_realm_IDs.append(id)
    return connected_realm_IDs


def find_realm_ID(name, connected_realm_IDs, access_token):
    found = 0
    REALM_NAME = name
    for id in connected_realm_IDs:
        if found == 1:
            break
        # Retrieve info for specific server ID
        connected_realm_info = make_request(
            f'{id}?namespace=dynamic-eu&locale=en_GB&access_token={access_token}')
        realms = connected_realm_info['realms']
        for realm in realms:
            if realm['name'] == REALM_NAME:
                print(f'Connected realm id: {id}, Realm id: {realm["id"]}')
                return id, realm['id']


def retrieve_token(client_id, client_secret, region='eu'):
    url = f'https://{region}.battle.net/oauth/token'
    body = {'grant_type': 'client_credentials'}
    auth = HTTPBasicAuth(client_id, client_secret)

    response = requests.post(url, data=body, auth=auth)
    return response.json()


def make_request(url, search=0):
    base_url = 'https://eu.api.blizzard.com/data/wow/{}connected-realm/'.format('' if search == 0 else 'search/')
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

connected_realm_IDs = get_connected_realm_ids(access_token)

# Find realm ID by its name
# server_id = find_realm_ID('Doomhammer', connected_realm_IDs, access_token)

server_id = 1402  # Doomhammer EU server ID, found by find_realm_ID function

# Doomhammer server AH data
ah_data = get_ah_data(server_id, access_token)
print('Hello')
