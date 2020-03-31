from requests import get, post
from pprint import pprint

from srcipts.requests.common import URL

tokens = post(f'{URL}/signin', json={'nickname': 'Roman',
                                     'unhashed_password': 'сильныйпароль'}).json()
pprint(tokens)
headers = {'Authorization': f'Bearer {tokens["access_token"]}'}

pprint(get(f'{URL}/friends_check', headers=headers).json())

pprint(post(f'{URL}/friend_add/2', headers=headers).json())
pprint(post(f'{URL}/friend_add/3', headers=headers).json())
