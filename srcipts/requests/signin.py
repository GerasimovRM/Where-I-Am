from requests import post

from srcipts.requests.common import URL


print(post(f'{URL}/signin', json={'nickname': 'Имя1123',
                                  'unhashed_password': 'сильныйпароль'}).json())