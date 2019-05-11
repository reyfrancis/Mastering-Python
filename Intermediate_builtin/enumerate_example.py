''' Enumerate is used when we want to find out the index of each item in a list 
As this code do: ''' 

example = ['left','right','up','down']

# for i in range(len(example)):
#     print(i, example[i])

# Can be done exactly by using enumerate without having to define 'i'.
for item_number, each_item in enumerate(example):
	print(item_number, each_item)
new_list = enumerate(example)

# The enumerate function returns a tuple of which, the first is the count and 
# The second item is the value from the list.
print('\n')

example_dict = {'left':'<','right':'>','up':'^','down':'v',}
print(example_dict)
print('\n')

# You can also make a dicitionary out of enumerate
# by using 'dict(enumerate(some_list/dict))'
new_dict = dict(enumerate(example))
print(new_dict)