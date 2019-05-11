''' Passing INSTANCE as ARGUMENT in another INSTANCE.
Say we want to have HR in our company and they take note of every Employee.
Now we want to find out all the names of the employee in the company that was hired '''

class Employee:
    raise_percentage = 5
    def __init__(self, first_name, last_name, pay):  
        self.first_name = first_name
        self.last_name = last_name
        self.email = '{}_{}@gmail.com'.format(first_name,last_name)
        self.pay = pay

class Developer(Employee):
    raise_percentage = 10
    def __init__(self, first_name, last_name, pay, prog_lang, github_repo):
        super().__init__(first_name, last_name, pay)    
        self.prog_lang = prog_lang
        self.github_repo = github_repo

class Engineer(Employee):
    raise_percentage = 15
    def __init__(self, first_name, last_name, pay, CAD_soft):
        super().__init__(first_name, last_name, pay)    
        self.CAD_soft = CAD_soft

class HR(Employee):
    raise_percentage = 8
    def __init__(self, first_name, last_name, pay, hired_employees=None):

        # Take note! An important thing to remember. Here hired_employees is a list
        # but is set default to 'None'. And later will be changed into an empty list 'self.hired_employees = []'
        # The reason why we did not set the ARGUMENT into just an empty list is: It's not recommended
        # to pass mutable data types such as list and dict in the default argument or in the argument.

        super().__init__(first_name, last_name, pay)
        if hired_employees is None:
            self.hired_employees = []
        else:
            self.hired_employees = hired_employees

    def add_employees(self, employee_INSTANCE):
        if employee_INSTANCE not in self.hired_employees:
            self.hired_employees.append(employee_INSTANCE)

    def print_all_employees(self):
        for i in range(len(self.hired_employees)):
            print(self.hired_employees[i].email)



employee_1 = Employee('Bob', 'Charlie', 30)
employee_2 = Employee('Amy', 'Donald', 30)
dev_1 = Developer('James', 'Harden', 50, 'Python', 10)
dev_2 = Developer('Lebron', 'James', 60, 'C++', 7)
eng_1 = Engineer('Steph', 'Curry', 100, 'AutoCad')

hr_1 = HR('Queen', 'Sarah', 30, [employee_1])
# Do not forget to enclose the last argument in a list, so that we can define the argument as list.

hr_1.print_all_employees()
print('\n')

hr_1.add_employees(employee_2)
# We dont enclose them in brackets anymore since we are appending them into the existing list 'self.hired_employees'.
hr_1.add_employees(dev_1)
hr_1.add_employees(dev_2)
hr_1.add_employees(eng_1)
hr_1.print_all_employees()
print('\n')



#isinstance() and issubclass()
#We can use this functions to know if an instance is an instance of a class
#and a class is a subclass of a parent's class

print(isinstance(dev_1, Developer))
print(isinstance(eng_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Employee, Developer))