from requests import post

print(post('https://wia-perm.herokuapp.com/api/v1/user', json={'nickname': 'Имя1',
                                                                'first_name': 'Тоже имя',
                                                                'last_name': 'Не имя',
                                                                'email': 'my_emai2l@k.k',
                                                                'unhashed_password': 'сильныйпароль'}).json())