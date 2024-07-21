def all_variants(text):
    for ln in range(len(text)):
        for st in range(len(text) - ln):
            print(st, ln, text[st:ln])



all_variants("abc")

# a = all_variants("abc")
# for i in a:
#     print(i)

