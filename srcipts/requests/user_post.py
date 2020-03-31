from requests import post

from srcipts.requests.common import URL


tokens = post(f'{URL}/signin', json={'nickname': 'Roman',
                                     'unhashed_password': 'сильныйпароль'}).json()
print(tokens)
headers = {'Authorization': f'Bearer {tokens["access_token"]}'}

print(post(f'{URL}/users', json={'nickname': 'Имя1',
                                'first_name': 'Тоже имя',
                                'last_name': 'Не имя',
                                'email': 'my_emai2l@k.k',
                                'unhashed_password': 'сильныйпароль'},
           headers=headers).json())
