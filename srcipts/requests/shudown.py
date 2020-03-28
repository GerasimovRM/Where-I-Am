from requests import get

from srcipts.requests.common import URL


print(get(f'{URL}/shutdown').json())
