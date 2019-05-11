''' Python Object-Oriented Programming
'METHOD' - is a function associated with a clas
'ATTRIBUTE' - is a data associated with a class
All credits to @Corey Schafer on his excellent tutorial on OOP '''

class Employee:
    pass


# INSTANCE - We can think of an instance as 'BIRTH' or 'CONSTRUCTION' of something.
# So if we pass an instance of class Employee. We are making a Employee.
# That means, if we pass two instances, then we made two employees as well.
employee1 = Employee()
employee2 = Employee()
# To check that both instances passed are unique, we can print their memory addresses and see that they are not equal.

print(employee1)
print(employee2)
if employee1 != employee2:
    print('They are not the same!')
print('\n')

# To understand very well the purpose or OOP itself, we need to cite a program and implementation on how to do it.
# Say we want to make a program that tracks Employees records.
employee1.first_name = 'Bob'
employee1.last_name = 'Charlie'
employee1.email = 'Bob_Charlie@gmail.com'

employee2.first_name = 'Amy'
employee2.last_name = 'Donald'
employee2.email = 'Amy_Donald@gmail.com'

# So, if we want to print employee1 first name:
print(employee1.first_name)

# And if somehow our company hired more employees, the pattern continues on adding each employees records
# employeen.first_name = 'First Name'
# employeen.last_name = 'Last Name'
# employeen.email = 'First Name_Last Name@gmail.com'

# Go to the next file to continue!