#Timeit module
#Sometimes we want our codes to run as fast as they can.
#And we optimize our codes for such problem, one way of optimizing it is to actually 
#time it. 

import timeit

print(timeit.timeit('''
input_list = range(100)

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = [i for i in input_list if div_by_five(i)]''', number=1000000))

#To use time it. Comment all the code to run, then the "number =" refers to how many times
#iterate the code