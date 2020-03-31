from requests import get, post, delete
from pprint import pprint

from srcipts.requests.common import URL

tokens = post(f'{URL}/signin', json={'nickname': 'Roman',
                                     'unhashed_password': 'сильныйпароль'}).json()
pprint(tokens)
headers = {'Authorization': f'Bearer {tokens["access_token"]}'}

pprint(delete(f'{URL}/user/4', headers=headers).json())