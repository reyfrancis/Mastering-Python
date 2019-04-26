#Different method for String concatenation

#1. Plus sighn
#One of the most basic ways to concatenate strings to use the 'plus' sign.

names = ['Tom', 'Jerry']

for name in names:
	statement = 'Hi ' + name
	print(statement)
print('\n')

#2. .join
#This is a good choice if concatenating onyl two strings, 
#however if concatenating two or more strings, .join is a better choice.

for name in names:
	statement = ' '.join(['Hello there', name])
	print(statement)
print('\n')

#Another example of .join is joining many strings

names.append('Oggy')
names.append('Cockcroaches')

print(', '.join(names))
print('\n')


#3. .format
#If we are concatenating our strings with different variables. 
#This method could be a great choice.

rat = 'Tom'
cat = 'Jerry'
dog = 'Oggy'
Cockcroaches = 'Cockcroaches'

print('{} chases {} while {} fights the {}.'.format(cat, rat, dog, Cockcroaches))