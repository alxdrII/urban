def custom_write(file_name, strings):
    control_write = {}
    count = 0

    file = open(file_name, "w", encoding="utf-8")

    for string in strings:
        count += 1
        control_write[(count, file.tell())] = string
        file.write(string + "\n")

    file.close()

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
