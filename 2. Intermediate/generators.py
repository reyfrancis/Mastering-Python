''' Generators dont return values. They are used to hold values inside a function without calling a variable. A very short and simple example to is to hold the 3 words and print them out. '''

def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'


for i in simple_gen():
    print(i)

print('\n')


CORRECT_COMBO = (3, 6, 1)
# This part is not really about generators but how to minimize the time in iterating to find a correct value instead of brute force.

# for c1 in range(10):
#     for c2 in range(10):
#         for c3 in range(10):
#             if (c1, c2, c3) == CORRECT_COMBO:
#                 print('Found the combo:{}'.format((c1, c2, c3)))

found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
			break
        for c3 in range(10):
        	if (c1, c2, c3) == CORRECT_COMBO:
        		print('Found the combo:{}'.format((c1, c2, c3)))
        		found_combo = True
        		break

# This is another example of holding values inside a function using yield
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo:{}'.format((c1, c2, c3)))
        break