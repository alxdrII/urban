from time import sleep
from threading import Thread
from datetime import datetime

def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count+1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()

wite_words(10, "example1.txt")
wite_words(30, "example2.txt")
wite_words(200, "example3.txt")
wite_words(100, "example4.txt")

time_finish = datetime.now()
print(f"Работа потоков {time_finish - time_start}")

threads = [
    Thread(target=wite_words, args=(10, "example5.txt")),
    Thread(target=wite_words, args=(30, "example6.txt")),
    Thread(target=wite_words, args=(200, "example7.txt")),
    Thread(target=wite_words, args=(100, "example8.txt"))
]
for tr in threads:
    tr.start()

for tr in threads:
    tr.join()

time_end = datetime.now()
print(f"Работа потоков {time_end - time_finish}")
