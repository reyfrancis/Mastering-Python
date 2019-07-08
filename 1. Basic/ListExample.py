''' List are the one of the programming features that Python supports particularly well.
 If you use list in other programming language, you don't have quite the flexibility in Python.
 In much of programming, 'array' is the more general term rather than list. '''

list1 = [1, 2, 3]
list2 = [4, 5, 6, 7]


# 1. list1 + list2
# Adding list
my_list = list1 + list2
print(my_list)
print('\n')


# 2. list.append()
# Using list.append adds another index from the last index of the list. Say the list has 5 indexes, that is, list[0], list[1], ... list[4], then using append will create another index on list[5].
my_list.append(8)
print(my_list)
print('\n')


# 3. varname[a:b]
# Slicing methods
print(my_list[0:3])    # Get the first 3 elements
print(my_list[4:6])    # Get the 5th to 6th element
print(my_list[:3])     # Get the first 3 elements
print(my_list[-3:])    # Get the last 3 elements
print(my_list[:])      # Get all the elements
print('\n')


# 4. list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list.append(list1)
my_list.append(list2)
my_list.append('END')
print(my_list)
# It is okay in Python to have any type of variable inside a list, may it be a float or integer, or string.