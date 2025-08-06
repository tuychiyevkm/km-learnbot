from pprint import pprint
import requests
from settings import TOKEN

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"


r=requests.get(url)
data = r.json()

result = data["result"]

last_update = result[-1]


pprint(last_update)