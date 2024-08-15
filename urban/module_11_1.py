import requests
from PIL import Image
import glob, os


def place_by_zip(zip: int) -> str:
    """Возвращает город и область по индексу"""

    rec = requests.get(f"https://kladr-api.ru/api.php?contentType=building&limit=1&withParent=1&zip={zip}").json()
    try:
        result = rec['result'][0]['parents']
        return f"{zip} {result[0]['name']} {result[0]['type']} {result[1]['type']} {result[1]['name']}"
    except IndexError:
        return ""


def resize_picture():
    """Изменяет размеры всех рисунков из папки pictures_in и копируя их в папку pictures_out"""


size = 128, 128

for infile in glob.glob(".\\pictures_in\\*.jpg"):
    file, ext = os.path.splitext(infile)
    with Image.open(infile) as im:
        im.thumbnail(size)
        im.save(file + ".jpg", "JPEG")



# print(place_by_zip(601501))
# print(place_by_zip(170001))
# print(place_by_zip(173001))

# for i in range(123, 1000):
#     res = place_by_zip(i*1000 + 1)
#     if res:
#         print(res)
