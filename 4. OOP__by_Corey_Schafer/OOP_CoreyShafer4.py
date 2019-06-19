''' Subclassing is useful whenever we have a general class and we want to create a more specific class 
and inherit the attributes from the general class. '''

# Say for our example, we have an Employee class. And we want to hire Developers, Designers, and Engineers to  
# work on our team. Well, each category might need another attribute, say, in the Developers they will need
# what programming language do they know, in the Engineer, what CAD software do they know
# And instead of writing a whole new class like this. 

'''
class Developer:

    def __init__(self, first_name, last_name, pay, prog_lang, github_repo):  
            self.first_name = first_name
            self.last_name = last_name
            self.email = '{}_{}@gmail.com'.format(first_name,last_name)
            self.pay = pay
            self.prog_lang = prog_lang
            self.github_repo = github_repo
class Engineer:

    def __init__(self, first_name, last_name, pay, CAD_soft):  
            self.first_name = first_name
            self.last_name = last_name
            self.email = '{}_{}@gmail.com'.format(first_name,last_name)
            self.pay = pay
            self.prog_lang = prog_lang
            self.github_repo = github_repo
'''

# To avoid that, we could use our Employee class to inherit all the basic attributes and pass them into our new classes.
class Employee:

    raise_percentage = 5

    def __init__(self, first_name, last_name, pay):  
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}_{}@gmail.com'.format(first_name,last_name)
        self.pay = pay

# First is we need to write down the name of the class and pass as argument the PARENT'S CLASS.
class Developer(Employee):
# Next is we call __init__ and pass all the arguments we would want to have.
    def __init__(self, first_name, last_name, pay, prog_lang, github_repo):
    # Then, we INHERIT from our PARENT CLASS / Employee class all our ATTRIBUTES that we want to have from them.
        super().__init__(first_name, last_name, pay)    #take note that we are not passing 'self' in this line.
        # Although, we could do this in a more familiar fashion.
        # Employee.__init__(self, first_name, last_name, pay).
        # It is recommended to use super() since it is much easier to understand.
        self.prog_lang = prog_lang
        self.github_repo = github_repo


dev_1 = Developer('James', 'Harden', 50, 'Python', 10)
employee1 = Employee('Bob', 'Charlie', 30)
employee2 = Employee('Amy', 'Donald', 30)
    

''' Help function is used to get the varialbes and functions under a class
Uncomment to see function! '''

print(help(Developer)) 

# Here we can see at the bottom that we also inherit the class variable raise_percentage = 5.
# To change that value

# 1. SUBCLASS.VARIABLE = VALUE
Developer.raise_percentage = 10

print(dev_1.raise_percentage)
print('\n')
print(employee1.raise_percentage)
print(employee2.raise_percentage)
print('\n')

# 2. Under the Subclass, redefine the variable
# class Developer:
#   raise_percentage = 10


# Aside from getting class variables from using help()
# We can also see the Method Resolution Order

# Method resolution order:
#  |      Developer
#  |      Employee
#  |      builtins.object

# We can see that the Python will find first the __init__() function from the Developer's class
# If its not in the Developer's class, it will try to find under the Employee's class 
# and lastly in the builtins.