import requests


def place_by_zip(zip: int) -> str:
    """Возвращает город и область по индексу"""

    rec = requests.get(f"https://kladr-api.ru/api.php?contentType=building&limit=1&withParent=1&zip={zip}").json()
    try:
        result = rec['result'][0]['parents']
        return f"{zip} {result[0]['name']} {result[0]['type']} {result[1]['type']} {result[1]['name']}"
    except IndexError:
        return ""


print("--- Работа с библиотекой 'requests': получаем данные с сайта 'https://kladr-api.ru/api.php' по индексу:")
print(place_by_zip(601501))
print(place_by_zip(170001))
print(place_by_zip(173001))
