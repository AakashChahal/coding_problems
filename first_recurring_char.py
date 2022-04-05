
#? Given an array = [2,5,1,2,3,5,1,2,4]:
#? It should return 2

#? Given an array = [2,1,1,2,3,5,1,2,4]:
#? It should return 1

#? Given an array = [2,3,4,5]:
#? It should return undefined

def first_recurring_char(inp_list):
    inp_dict = {}
    for inp in inp_list:
        if inp in inp_dict.keys():
            return inp
        else:
            inp_dict[inp] = True

    return None

print(first_recurring_char([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_char([2, 3, 4, 5]))