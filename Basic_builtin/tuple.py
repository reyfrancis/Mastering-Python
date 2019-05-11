'''Tuples are very similar to list, however there values can't be changed. 
 Tuples can be made by using parenthesis instead of square brackets '''

# 1. tuple = (1, 2, 3, 4)
my_tuple = (1, 2, 3, 4, 'END')
print(my_tuple)
# Accesing the value of tuples are just the same with list, however we can never change its values.


# 2. Slicing
print(my_tuple[3:5])   #getting the 4th and 5th element

# 3. Appending
my_tuple += my_tuple
print(my_tuple)


# 4. Change value
try:
    my_tuple[0] = 'CHANGED'
except TypeError:
        print('Error changing!')
try:
    del my_tuple[0]
except TypeError:
        print('Error deleting!')