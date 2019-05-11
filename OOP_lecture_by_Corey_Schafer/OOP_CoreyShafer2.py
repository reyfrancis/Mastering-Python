''' To simplify things are written, OOP is made '''

class Employee:

    # Ignore for now, get back later.
    raise_percentage = 5


    # Ignore for now, get back later.
    num_employees = 0


    # def __init__ is where we define our Attributes of our class/object.
    def __init__(self, first_name, last_name, pay):  
    # 'self' is always the first argument although is not required to name it as self.
    # But conventionally, this is how programmers naming it.
        self.first_name = first_name
        # Take note that the left 'first_name' or the self.first_name is an attribute of the class
        # and the right 'first_name' is an argument inside def __init__()
        # They are not required to be the same, say:

        # self.first_name = first
        # self.firstName = first_name
        # It is just conventional to programmers to use the same words in attributes and arguments

        self.last_name = last_name
        self.email = '{}_{}@gmail.com'.format(first_name,last_name)
        self.pay = pay

        # Ignore for now, get back later.
        Employee.num_employees += 1

    # Ignore for now, get back later.
    def fullname(self):
        print('{} {}'.format(self.first_name, self.last_name))


    # Ignore for now, get back later.
    def apply_raise(self):
        self.pay = float(self.pay*(100+self.raise_percentage)/100)
        # Take note that we can't access 'raise_percentage' as it will throw an error.
        # Class Variables could be accessed using 3 ways:

        # CLASS.VARIABLE -> Employee.raise_percentage
        # INSTANCE.VARIABLE -> employee1.raise_percentage
        # self.VARIABLE -> self.raise_percentage

        # INSTANCE.VARIABLE and self.VARIABLE has no difference except that self is for all instances
        # while INSTANCE.VARIABLE is for that specific INSTANCE
        print(self.pay)

# Creating instances
employee1 = Employee('Bob', 'Charlie', 30)
employee2 = Employee('Amy', 'Donald', 30)

# Printing the email
print(employee1.email)
print('\n')

# Now moving to methods, say we want to print the full name of our employees.
print('{} {}'.format(employee1.first_name, employee1.last_name))
print('\n')

# However, again, if we want to print out another employees name, we would have to write the whole code again.
# And this is where METHODS comes into play, see 'def fullname():'

employee1.fullname()
employee2.fullname()
print('\n')
# Now instead of typing the whole code. We just have to call the proper self to print the full name.
# There are two ways to call a method inside a class

# 1.INSTANCE.METHOD
employee1.fullname()   # employee1 = Instance
                       # fullname() = Method

# 2. CLASS.METHOD(INSTANCE)
Employee.fullname(employee1)   # Employee = Class
                               # fullname = method
                               # employee1 = Instance
print('\n')


''' Class Variables '''
# Say we want to increase the wages of our employees and clearly not all employees would have 
# the same increase every year.
# So say for example, that the company offers a standard increase of 5% each year.
# And a bonus of another 5% to those outstanding employees.
# And we want to print out their new salary after the increase.
# @See 'def apply_raise():' and 'raise_percentage = 5'.

employee1.apply_raise()
employee2.apply_raise()
print('\n')


# And say, employee2 is outstanding and employee1 is not.
# And so we need to change 'raise_percentage' value for employee2.
# However, changing class variable would change for employee1 as well.
Employee.raise_percentage = 10 
employee1.apply_raise()
employee2.apply_raise()
print('\n')

Employee.raise_percentage = 5   # Bring back the percentage to 5 

# Well, instead of changing the class variable, we could add the class variable as an attribute to an instance.
# Using .__dict__ will show the attributes of class or a instance
# To check all attributes of instance employee1 and class Employee
print('INSTANCE ATTRIB: {}'.format(employee1.__dict__))
print('\n')
print('CLASS ATTRIB: {}'.format(Employee.__dict__))
print('\n')

# We can see that the instance has no attribute raise_percentage but the class have.
# So we add raise_percentage as attribute for the instance.
employee1.raise_percentage = 10
print('INSTANCE ATTRIB_NEW: {}'.format(employee1.__dict__))
print('\n')
print('CLASS ATTRIB_NEW: {}'.format(Employee.__dict__))
# And from here we can instance value of raise_percentage without changing the class raise_percentage.
print('\n')

employee1.apply_raise()
employee2.apply_raise()
print('\n')

# And lets say we want to count how many employees do we have.
# We would want to have a function inside __init__ that adds everytime it is being executed.
# @See 'num_employees = 0' and 'Employee.num_employees += 1' under __init__.
print(Employee.num_employees)