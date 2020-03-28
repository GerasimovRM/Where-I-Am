from requests import post

from .common import URL


print(post(f'{URL}/signin', json={'nickname': 'Roman',
                                  'unhashed_password': 'сильныйпароль'}).json())