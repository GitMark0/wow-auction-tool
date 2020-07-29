import requests

client_id = '4765849c9d3a4ae7a1132515105cba14'
client_secret = '0rR3xvKEtE56pjSMdT16i3DO6pEPf0eM'
data = {'grant_type': 'client_credentials'}

# Response is a dictionary with k, v pairs:
# "access_token": "USVb1nGO9kwQlhNRRnI4iWVy2UV5j7M6h7",
# "token_type": "bearer",
# "expires_in": 86399,
# "scope": "example.scope"

response = requests.post('https://eu.battle.net/oauth/token', data=data, auth=(client_id, client_secret)).json()
