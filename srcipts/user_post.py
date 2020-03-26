from requests import post

print(post('http://localhost:5000/api/v1/user', json={'nickname': 'Имя',
                                                      'first_name': 'Тоже имя',
                                                      'last_name': 'Не имя',
                                                      'email': 'my_email@k.k',
                                                      'unhashed_password': 'сильныйпароль'}).json())