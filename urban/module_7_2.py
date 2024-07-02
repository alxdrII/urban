def custom_write(file_name, strings):
    control_write = {}

    with open(file_name, "w", encoding="utf-8") as file:
        for index, string in enumerate(strings, start=1):
            control_write[(index, file.tell())] = string
            file.write(string + "\n")

    return control_write


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
