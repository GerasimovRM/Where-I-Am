from requests import post

from srcipts.requests.common import URL


print(post(f'{URL}/signin', json={'nickname': 'Roman',
                                  'unhashed_password': 'сильныйпароль'}).json())