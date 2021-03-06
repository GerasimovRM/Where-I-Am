from requests import get, post
from pprint import pprint

from srcipts.requests.common import URL

tokens = post(f'{URL}/signin', json={'nickname': 'Roman',
                                     'unhashed_password': 'сильныйпароль'}).json()
pprint(tokens)
headers = {'Authorization': f'Bearer {tokens["access_token"]}'}

pprint(get(f'{URL}/user/100', headers=headers).json())
pprint(get(f'{URL}/user/1', headers=headers).json())
pprint(get(f'{URL}/users', headers=headers).json())
