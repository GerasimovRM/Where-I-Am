from requests import get

print(get('http://localhost:5000/api/v1/shutdown').json())