import os
from pathlib import Path
# for root, dirs, files in os.walk(".", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

ptath = r"S:\Python\Code\MegaMail"
ptest = './test.py'

# for root, dirs, files in os.walk(r"S:\Python\Code\MegaMail", topdown=True):
#    # for name in files:
#    #    print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

# roots = next(os.walk(ptath))[0]
# print(roots)
# print(ptest.parents)

# current_path = os.path.dirname(os.path.abspath(__file__))
# print(current_path)
# parent = os.path.dirname(current_path)
# print("Parent directory", parent)
# roots = next(os.walk(parent))[1]
# print(roots)

# p = Path(__file__).parents[1]
# p_string = str(p)
# roots = next(os.walk(p))[1]
# print(roots)
# temp_path = p_string + r'\temp'
# print('temp path', temp_path)
#
# if 'contact_data' in roots:
#    print('True')

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

list = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 7]
list3 = intersection(list, list2)
print(list3)