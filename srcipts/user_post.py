from requests import post

print(post('http://localhost:5000/api/v1/user', json={'nickname': 'Имя2',
                                                      'first_name': 'Тоже имя',
                                                      'last_name': 'Не имя',
                                                      'email': 'my_email2@k.k',
                                                      'unhashed_password': 'сильныйпароль'}).json())