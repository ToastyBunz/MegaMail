import os

# real_path = 'S:/DevStuff/EmailTesting.xlsx'
# bad_path = 'S:\DevStuff\EmailTesting.xlsx' #this accually works but is dangers if there is a \t or \n
#
# fixed_path = bad_path.replace("\\", '/')
# print(fixed_path)
#
# def path_exists(path):
#     return print(os.path.exists(path))
#
# path_exists(bad_path)

str = 'NathaN'
print(str[0])
str = str[1:]
str = str[:-1]
print(str)