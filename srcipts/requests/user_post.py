from requests import post

from .common import URL

print(post(f'{URL}/user', json={'nickname': 'Имя1',
                                'first_name': 'Тоже имя',
                                'last_name': 'Не имя',
                                'email': 'my_emai2l@k.k',
                                'unhashed_password': 'сильныйпароль'}).json())