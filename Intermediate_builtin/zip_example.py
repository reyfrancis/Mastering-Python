#Zip
#The zip function iterates through a list and aggregates(merge) them.
#There are lot of ways to combine two list and here are some:


x = [1, 2, 3, 4]
y = [7, 8, 9, 10]
z = ['a', 'b', 'c', 'd']

#1. for a,b in zip(x,y)

for a,b,c in zip(x,y, z):
	print(a, b)
print('\n')


#Also, aside from printing merged lists. 
#Zip also creates a memory wher the merged list and this can be converted
#to a list or tuple or dict

#2. Converting to a list

new_list = []

for i in range(len(x)):
	new_list.append(list(zip(x, y)))
print(new_list)
print('\n')

#3. Converting to a dict

new_dict = {}

# for i in range(len(x)):
# 	#TODO: append for a dict
# 	new_dict.append(dict(zip(x, y))) 
# print(new_dict)