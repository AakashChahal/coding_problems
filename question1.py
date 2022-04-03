# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
# For Example:
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'i'];
# should return false.
# -----------
# const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
# should return true.

# 2 parameters - arrays - no size limit
# return true or false

def answer(arr1, arr2):
    common_dict = {}

    for el in arr1:
        if el in arr2:
            common_dict[el] = True
        else:
            common_dict[el] = False

    for val in common_dict.values():
        if val:
            return True

    return False

arr1 = ['a', 'b', 'c', 'x']
arr2 = ['z', 'y', 'x']

print(answer(arr1, arr2))