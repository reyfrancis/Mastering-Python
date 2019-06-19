class Employee:

    raise_percentage = 5
    num_employees = 0

    def __init__(self, first_name, last_name, pay):  
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}_{}@gmail.com'.format(first_name,last_name)
        self.pay = pay
        Employee.num_employees += 1

    def fullname(self):
        print('{} {}'.format(self.first_name, self.last_name))

    def apply_raise(self):
        self.pay = float(self.pay*(100+self.raise_percentage)/100)
        print(self.pay)

    @classmethod
    def change_raise_percentage(cls, new_raise):   # def change_raise_percentage(ARGUMENT1, ARGUMENT2)
        cls.raise_percetage = new_raise            # cls.ATTRIBUTE = ARGUMENT2'

    @classmethod   # This is called 'DECORATOR'
    def from_splitstring(cls, employee_string):   # It is again a common convention that programmers name their 
                                                  # constructor class methods as something that starts with 'from_(WHAT_FUNCTION)'
        first_name, last_name, pay = employee_string.split('-')
        return cls(first_name, last_name, pay)

    @staticmethod
    def check_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

# Creating instances
employee1 = Employee('Bob', 'Charlie', 30)
employee2 = Employee('Amy', 'Donald', 30)

# Class Methods can be used to changed value of class variables 
# Or act as a some_function + constructor

# Say we want to change the value of raise_percetage to 20
# We can do that in two ways

# 1.CLASS.VARIABLE = VALUE
Employee.raise_percetage = 20
print(Employee.raise_percetage)
print(employee1.raise_percetage)
print(employee2.raise_percetage)
print('\n')

# 2. Class Method
# In order to make a classmethod, we write first @classmethod
# Then everything is the same except that the first argument is 'cls' and not 'self'
# There is really no rule to what should be named for the first argument. But it became a convention
# by programmers to name the first argument of class method as 'cls'
# @See 'def change_raise_percentage'
employee1.change_raise_percentage(30)
print(employee1.raise_percetage)
print('\n')


''' Class Methods as Constructor '''

# Say we have a file that have employees data that looks like this: Bob-Charlie-30.
# And we want to make a split function and after splitting will automatically create our employee profile.
# @See 'def from_splitstring'.
employee3 = Employee.from_splitstring('Winnie-Poo-10')
print(employee3.email)
print('\n')

''' Static Methods '''
# Static methods are functions that are written inside the class but don't use any instances or attributes.
# In other words, it doesn't need to have 'self' or 'cls' as its first argument.
# So for example, we wanted to know if a certain date is a workday or not and we want it to include 
# in our Employee class then, we should make it as static method.
import datetime

my_date = datetime.date(2019, 8, 5)
print(Employee.check_workday(my_date))