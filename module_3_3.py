
def print_params(a = 1, b = 'строка', c = True):
#    print(values_list)
#    print(values_dict)
    print(a, b, c)
    
# print_params()
# print_params(a = 2, b = 'Lada', c = False)
# print_params(b = 25)
# print_params(c = [1,2,3])

values_list = ['Lada', 1999, 29.10]
values_dict = {'a': 'Lada', 'b': 1999, 'c': 29.10}
values_list_2 = [1999, 'LadaDzenis']


#print_params(*values_list)
#print_params(**values_dict)
print_params(*values_list_2, 42)

