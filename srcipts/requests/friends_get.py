from requests import get, post
from pprint import pprint

from srcipts.requests.common import URL

tokens = post(f'{URL}/signin', json={'nickname': 'Fedor',
                                     'unhashed_password': '123'}).json()
pprint(tokens)
headers = {'Authorization': f'Bearer {tokens["access_token"]}'}

pprint(get(f'{URL}/friends', headers=headers).json())
