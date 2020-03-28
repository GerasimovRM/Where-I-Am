from requests import post

from srcipts.requests.common import URL


print(post(f'{URL}/signup', json={'nickname': 'Имя1123',
                                'first_name': 'Тоже имя',
                                'last_name': 'Не имя',
                                'email': 'my_emai2332l@k.k',
                                'unhashed_password': 'сильныйпароль'}).json())