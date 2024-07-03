class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self) -> dict:
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, encoding="utf-8") as file:
                    all_words[file_name] = [s.strip(",.=!?;:- ").lower() for s in file.read().split()]

            except FileNotFoundError:
                print(f'Невозможно открыть файл {file_name}')

            except:
                print(f'Ошибка при работе с файлом {file_name}')

        return all_words

    def __func(self, word: str, fn="index"):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name in self.file_names:
            if word in all_words[file_name]:
                if fn == "index":
                    result[file_name] = all_words[file_name].index(word) + 1

                elif fn == "count":
                    result[file_name] = all_words[file_name].count(word)

        return result

    def find(self, word: str) -> dict:
        return self.__func(word, 'index')

    def count(self, word: str) -> dict:
        return self.__func(word, 'count')


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))
