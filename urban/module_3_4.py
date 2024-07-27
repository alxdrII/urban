def single_root_words(root_word, *other_words):
    #same_words = list(filter(lambda x: x.lower() in root_word.lower() or root_word.lower() in x.lower(), other_words))
    same_words = []
    for o_word in other_words:
        if o_word.lower() in root_word.lower() or root_word.lower() in o_word.lower():
            same_words.append(o_word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
