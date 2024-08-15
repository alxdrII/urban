import requests
from PIL import Image
import glob, os
import tkinter.filedialog as fd


def place_by_zip(zip: int) -> str:
    """Возвращает город и область по индексу"""

    rec = requests.get(f"https://kladr-api.ru/api.php?contentType=building&limit=1&withParent=1&zip={zip}").json()
    try:
        result = rec['result'][0]['parents']
        return f"{zip} {result[0]['name']} {result[0]['type']} {result[1]['type']} {result[1]['name']}"
    except IndexError:
        return ""


def resize_picture():
    """Изменяет размеры всех рисунков *.jpeg в выбранной папке"""

    directory = fd.askdirectory(title="Открыть папку с картинками", initialdir="./")
    if not directory:
        return -1

    size = 128, 128
    count = 0
    for infile in glob.glob(directory + "/*.jpeg"):
        file, ext = os.path.splitext(infile)
        with Image.open(infile) as im:
            im.thumbnail(size)
            im.save(file + "_sm" + ".jpg", "JPEG")
            count += 1

    return count


print("--- Работа с библиотекой 'requests': получаем данные с сайта 'https://kladr-api.ru/api.php' по индексу:")
print(place_by_zip(601501))
print(place_by_zip(170001))
print(place_by_zip(173001))
print()

print("--- Работа с библиотекой 'PIL': Меняем размер файлов .jpeg")
count = resize_picture()
print(f"Изменен размер у {count} рисунков.")
