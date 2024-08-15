import requests
import PIL
from pprint import pprint


def place_by_zip(zip: int) -> str:
    """Возвращает Город и область по индексу"""

    rec = requests.get(f"https://kladr-api.ru/api.php?contentType=building&limit=1&withParent=1&zip={zip}").json()
    try:
        result = rec['result'][0]['parents']
        return f"{zip} {result[0]['name']} {result[0]['type']} {result[1]['type']} {result[1]['name']}"
    except IndexError:
        return ""


def edit_picture():



for zip in range(123, 1000):
    res = place_by_zip(zip*1000 + 1)
    if res:
        print(res)