def single_root_words(root_word, *other_words):
    same_words = filter(lambda x: x.lower() in root_word.lower() or root_word.lower() in x.lower(), other_words)
    return list(same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)