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


