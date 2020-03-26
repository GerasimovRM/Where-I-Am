from requests import get
from pprint import pprint

pprint(get('http://localhost:5000/api/v1/user/-10').json())
pprint(get('http://localhost:5000/api/v1/user/2').json())
pprint(get('http://localhost:5000/api/v1/user').json())