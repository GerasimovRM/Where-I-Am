from requests import post

from srcipts.requests.common import URL


print(post(f'{URL}/signup', json={'nickname': 'Roman',
                                'first_name': 'Роман',
                                'last_name': 'Герасимов',
                                'email': 'romagrizly@gmail.com',
                                'unhashed_password': 'сильныйпароль'}).json())


print(post(f'{URL}/signup', json={'nickname': 'test',
                                'first_name': 'test',
                                'last_name': 'test',
                                'email': 'test@gmail.com',
                                'unhashed_password': 'сильныйпароль'}).json())

print(post(f'{URL}/signup', json={'nickname': 'Fedor',
                                'first_name': 'Федя',
                                'last_name': 'Федосов',
                                'email': 'test123fed@gmail.com',
                                'unhashed_password': '123'}).json())

print(post(f'{URL}/signup', json={'nickname': 'Fedordel',
                                'first_name': 'Федя',
                                'last_name': 'Федосов',
                                'email': 'test123delfed@gmail.com',
                                'unhashed_password': '123'}).json())


