#Using For-Loop to iterate functions can be done, mainly by using 

def printHi():
    print('Hi')


#1. for i in range():
#This is the most common way to iterate some functions or statements in python.
for i in range(10):
     printHi()
print('\n')

#However, we can also do it in 1 line of code:
#2. [function for i in range()]
[printHi() for i in range(10)]
#just take note that we should enclose them in a bracket.
#Sadly we can't use the print function inside the [function for i in range()] method

[print("Hi") for i in range(10)]
#This code will throw an error