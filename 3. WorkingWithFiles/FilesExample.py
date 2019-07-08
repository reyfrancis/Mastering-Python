'''Opening and closing files. 
There are a lot of ways to open and close files and here some'''

item = 1

def printTut():
	global item   #Used global variable to increase item value
	if item > 1:
		print('\n')
	print('Part: {}'.format(item))
	item += 1


# 1. f = open()
# Remember that whenever we use this method we should always type out.
# f.close() after using the file since it would cause later issues.
printTut()

f = open('test.txt', 'r')
print(f.name)
print(f.mode)
# print(f.read())
f.close



# 2. with open() as f:
# This method is much preferred since after this line of codes
# end, the file would be automatically closed without calling the f.close
printTut()

with open('test.txt', 'r') as f:
	print(f.name)
	print(f.mode)

# Now reading the .txt file also have a lot of options.


# 3. Reading the whole text
# If we want to read or to store the whole text
printTut()

with open('test.txt', 'r') as f:
	f_contents = f.read()
	print(f_contents)


# 4. Reading all the lines or storing each line to a list
printTut()

with open('test.txt', 'r') as f:
	new_list = f.readlines()

for i in range(len(new_list)):
	print(new_list[i])   #TODO: Stop printing new lines!
							


# 5. Reading line by line using readline()
# Take note that everytime we call readline(), it reads the next line.
# Much like of appending inside a list.
printTut()

with open('test.txt', 'r') as f:
	print(f.readline())
	print(f.readline())


# 6.The most efficient way to read line by line is to use for line in f: 
printTut()

with open('test.txt', 'r') as f:
	for line in f:
		print(line)


# Reading specific numbers of characters
# 7. f.read(number)
printTut()

with open('test.txt', 'r') as f:
	f_contents = f.read(12)
	print(f_contents)


# Reading character by character not line by lines
# 8. f.read(size_to_read)
printTut()

with open('test.txt', 'r') as f:
	f_contents = f.read(1)

	while len(f_contents) > 0:
		if f_contents != '\n':   #This option is to eleminate all the newlines at the end of each line
			print(f_contents)
		f_contents = f.read(1)

# 9. f.tell 
# f.tell() keeps track of where we are relative to the first character.
printTut()

with open('test.txt', 'r') as f:
	f_contents = f.read(5)   # Here we read 5 characters.
	print(f.tell())   # In which character are we now relative to the first character.
					  # Since we already read the first 5 characters. Then f.tell() would return 5.

# Now if we try to read again 3 more char.
	f_contents = f.read(3)
	print(f_contents)   # Notice that we start reading from the fifth character.

# To get back reading to start we use f.seek(Starting_Position), we pass '0' into the Starting_Position
# since we want to start from the very first char
	f.seek(0)
	f_contents = f.read(3)
	print(f_contents)


# 10. Overwriting to an existing file
# Here we have a file that has some text pre written inside that says "Dont overwrite me!".
printTut()

with open('overwrite.txt', 'w+') as f:		
# After this line of code is executed, the whole text in the file is all deleted or in programming term "TRUNCATED".									
# with open('filename.txt', 'w+') lets you read and write. Just remember that it deletes everything after execution.
	f.write('You are being overwritten! HAHA')
	f.seek(0)   # Need to place the index back to the starting point so it can read all the text. Otherwise, will output blank space
	print('New text: {}'.format(f.read()))


# 11. Not Overwriting to an existing file
# This line of code will write but will NOT truncate or delete all the text after execution.
printTut()

with open('overwrite.txt', 'r+') as f:   # will not delete all the text after this line is executed
	f_contents = f.read()
	f.seek(0)	
	f.write('You are NOT being overwritten! HOHO ')
	f.write(f_contents)
	f.seek(0)
	print('New text: {}'.format(f.read()))


# 12. Appending
# Instead of overwriting the file. We can append inside the file
# with open('overwrite.txt', 'a+') as f:
printTut()

with open('overwrite.txt', 'a+') as f:
# Will not delete all the text after this line is executed.
# It a+ is only different from r+ in indexing. If you call r+, the index automatically points to the first character
# or f.seek(0) while if you call a+, the index points to the last character f.seek(whole_text).
	f.write(' Appending . . .')
	f.seek(0)
	print('New text: {}'.format(f.read()))

# To wrap up. There are three additional modes: 'w+', 'r+' and 'a+' aside from 'r' and 'w'.
# It is also very important to make use of f.seek() and f.tell().
# Whenever we call f.read() or f.write(), the index always change depending on much we read or write.
# So to read all, always call f.seek(0) first before f.read() .


# 13. Copying line by line to another file.
# We can make a copy of a file directly, but if we want to copy it line by line, this is how its done.
printTut()

with open('test.txt', 'r') as f:
	with open('test_copy.txt', 'w') as g:	
	# If we already have the test_copy.txt then it will truncate the existing texts with the new texts.
	# However if we dont have yet, it will create test_copy.txt and write the new texts.								
		for line in f:
			g.write(line)
with open('test_copy.txt', 'r') as g:
	print(g.read())
# You notice that we copy all the text with newline 
# And NOT something like this 'mic check 1, 2, 312345END'
# That is because when we read each line it is being read like this
# mic check\n1, 2, 3\n1\n2\n3\n4\n5\nEND' where '\n' is a single and special character
# Try printing
print('\n')
print('mic check\n1, 2, 3\n1\n2\n3\n4\n5\nEND')


# 14. Copying picture or other file extensions line by line
# I have these 3 files. Bootstrap.mp4, Rey.jpg, PythonCookbook.pdf which I will make a copy using text line by line.
printTut()

# However if we read them line by line, it will throw an error!
try:
	with open('Rey.jpg', 'r') as f:
		with open('Rey_copy.jpg', 'w') as g:
			for line in f:
				g.write(line)
except:
	print('UnicodeDecodeError: utf-8 codec can\'t decode byte 0xff in position 0: invalid start byte')

# So in order to do that, we should read it in binary and write it in binary as well.
with open('Rey.jpg', 'rb') as f:
	with open('Rey_copy.jpg', 'wb') as g:
		for line in f:
			g.write(line)

# And a copy of pdf and mp4 as well.
with open('PythonCookbook.pdf', 'rb') as f:
	with open('PythonCookbook_copy.pdf', 'wb') as g:
		for line in f:
			g.write(line)

with open('Bootstrap.mp4', 'rb') as f:
	with open('Bootstrap_copy.mp4', 'wb') as g:
		for line in f:
			g.write(line)

# 14. Copying picture or other file extensions by specific size.
# Instead of doing it line by line. We will copy it in specifiz sizes.
specific_size = 10

with open('Rey.jpg', 'rb') as f:
	with open('Rey_copy_bysize.jpg', 'wb') as g:
		f_contents = f.read(specific_size)
		while len(f_contents) > 0:
			g.write(f_contents)
			f_contents = f.read(specific_size)   # Update the value of f_contents. Otherwise will go infinitely.