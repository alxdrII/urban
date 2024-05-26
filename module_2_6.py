def print_params(a=30, b='Vitaly', c=None):
    print(a, b, c)


# 1
print_params()
print_params(b='Dmitry')
print_params(c=[2001, 2005, 2011]),

# 2
values_list = [52, 'Swetlana', [1996, 1999]]
values_dict = {'a': 16, 'b': 'Tanya', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3
values_list_2 = [22, 'Sergey']
print_params(*values_list_2, [2023])