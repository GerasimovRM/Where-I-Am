from requests import get

from .common import URL


print(get(f'{URL}/shutdown').json())
