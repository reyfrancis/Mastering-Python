''' Explaining_FunctionActivation:
To explain how local and global variables work, we should tackle how a function is initialized
Having this simple code to get the maximum value '''

# def maxof(val1, val2):

#     if val1 > val2:
#         return val1
#     else:
#         return val2
        

a = 2
b = 3

# c = maxof(a, b)
# print(c)
# print('\n')

# When we run our program, the computer just read every def function and remember that its a function.
# Then we get into the main program, these are the stuff outside functions.
# In our example, the main program creates variables a = 2 and b = 3
# Then, it calls def maxof or what we call Function Activation.
# The value of both a and b are copied into val1 and val2. Remember 'COPIED'
# val1 and val2 doesn't even know that a and b exist, they just copied the value which are 2 and 3
# After executing the whole def maxof, the memory of val1 and val2 are now 'FREED' or 'DELETED'
# Hence, any attempt to recover val1 and val2's values will throw an error since the values are already deleted

try:
    print(val1)
except NameError:
    print('val 1 is not defined!')
print('\n')

# See that instead of saying val1 has no value. It returns that val1 is not defined
# Because val1 is a local variable which lurks inside the def maxof
# So the outside of the def maxof will not know that val1 exists!

# To solved this problem, we can use global variables. However we can't make val1 as global variable
# Since it is already a local variable passed as argument inside a function

# def maxof(local_variable, local_variable) 
# And if we try to make val1 as global:


# def maxof(val1, val2):
#     global val1
#     if val1 > val2:
#         return val1
#     else:
#         return val2

# Would throw
print('SyntaxError: name val1 is local and global')
print('\n')

# So we need to have another variable to set as global aside from val1.

'''Uncomment this code and Comment the above code!'''     

# val_global = 0

# def maxof(val1, val2):
#     global val_global
#     val_global = val1

#     if val1 > val2:
#         return val1
#     else:
#         return val2

# c = maxof(a, b)
# print('val_global value as global variable: {}'.format(val_global))
# print('\n')

# Easy, Right? HOWEVER it is not recommended or highly discouraged to use global variables since it can messesd up
# with your later codes. Instead, we can return two values and one of which is val1, and then reprint it again on the screen.

'''Uncomment this code and Comment the above code!'''  

def maxof(val1, val2):
    val_global = val1

    if val1 > val2:
        return val1, val1
    else:
        return val2, val1
    
c = maxof(a, b)
print('val1: {}'.format(c[1]))   # This is the proper way to get values or variables inside a function!