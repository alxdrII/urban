def all_variants(text):
    for ln in range(1, len(text)+1):
        for i in range(len(text)):
            if ln+i > len(text):
                break
            yield text[i:ln+i]


all_variants("abc")

a = all_variants("abc")
for i in a:
    print(i)
