def print_asterisk():
    print('*', end='')
def print_carriage_newline():
    print('\n \r', end='') 

# 1.
# * * * * * * * * * *
for i in range(10):
    print_asterisk()
print_carriage_newline()

print_carriage_newline()    

# 2. 
# * * * * * * * * * *
# * * * * *
# * * * * * * * * * * * * * * * * * * * *
for i in range(10):
    print_asterisk()
print_carriage_newline()
for i in range(5):
    print_asterisk()
print_carriage_newline()
for i in range(20):
    print_asterisk()
print_carriage_newline()

print_carriage_newline()

# 3. 
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
for i in range(10):
    for j in range(10):
        print_asterisk()
    print_carriage_newline()
print_carriage_newline()

# 4.
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
for i in range(10):
    for j in range(5):
        print_asterisk()
    print_carriage_newline()
print_carriage_newline()

# 5.
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
for i in range(5):
    for j in range(20):
        print_asterisk()
    print_carriage_newline()
print_carriage_newline()

# 6.
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
x = 0
for i in range(10):
    for j in range(10):
        print('{} '.format(x), end='')
        x+=1
    x = 0
    print_carriage_newline()
print_carriage_newline()

# 7. 
# 0 0 0 0 0 0 0 0 0 0 
# 1 1 1 1 1 1 1 1 1 1 
# 2 2 2 2 2 2 2 2 2 2 
# 3 3 3 3 3 3 3 3 3 3 
# 4 4 4 4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 5 
# 6 6 6 6 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 7 7 7 
# 8 8 8 8 8 8 8 8 8 8 
# 9 9 9 9 9 9 9 9 9 9 
x = 0
for i in range(10):
    for j in range(10):
        print('{} '.format(x), end='')
    x+=1
    print_carriage_newline()
print_carriage_newline()     

# 8.
# 0 
# 0 1 
# 0 1 2 
# 0 1 2 3 
# 0 1 2 3 4 
# 0 1 2 3 4 5 
# 0 1 2 3 4 5 6 
# 0 1 2 3 4 5 6 7 
# 0 1 2 3 4 5 6 7 8 
# 0 1 2 3 4 5 6 7 8 9 

x = 0
for i in range(10):
    for j in range(i+1):
        print('{} '.format(x), end='')
        x+=1
    x = 0
    print_carriage_newline()
print_carriage_newline()  

# Optimal Solution
# for row in range(10):
#     for column in range(row+1):
#         print (column,end=" ")
#     print()
# print_carriage_newline()  

# 9.
# 0 1 2 3 4 5 6 7 8 9 
#   0 1 2 3 4 5 6 7 8 
#     0 1 2 3 4 5 6 7 
#       0 1 2 3 4 5 6 
#         0 1 2 3 4 5 
#           0 1 2 3 4 
#             0 1 2 3 
#               0 1 2 
#                 0 1 
#                   0 
x = 0
for i in range(10):
    for j in range(10-i):
        if j == 0:
            for i in range(i):
                print('  ', end='')
        print('{} '.format(x), end='')
        x+=1
    x = 0
    print_carriage_newline()
print_carriage_newline()

# Optimal Solution  
# for row in range(10):
 
#     for j in range(row):
#         print (" ",end=" ")
 
#     for j in range(10-row):
#         print (j,end=" ")
 
#     print()

# 10.
x = 1
for i in range(9):
    for j in range(9):
        print('{} '.format(x), end='')
        x+=(i+1)
    x=i+2
    print_carriage_newline()
print_carriage_newline() 

# 11.
#                   1 
#                 1 2 1 
#               1 2 3 2 1 
#             1 2 3 4 3 2 1 
#           1 2 3 4 5 4 3 2 1 
#         1 2 3 4 5 6 5 4 3 2 1 
#       1 2 3 4 5 6 7 6 5 4 3 2 1 
#     1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 
#   1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 
x = 1
for i in range(10):
    for k in range(10-i):
        print('  ', end='')

    for j in range(i):
        print('{} '.format(x), end='')
        x+=1

    x-=1
    for j in range(i-1):
        x-=1
        print('{} '.format(x), end='')

    x = 1
    print_carriage_newline()
print_carriage_newline()  


# 12.                   
#                   1 
#                 1 2 1 
#               1 2 3 2 1 
#             1 2 3 4 3 2 1 
#           1 2 3 4 5 4 3 2 1 
#         1 2 3 4 5 6 5 4 3 2 1 
#       1 2 3 4 5 6 7 6 5 4 3 2 1 
#     1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 
#   1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 
#     1 2 3 4 5 6 7 8 
#       1 2 3 4 5 6 7 
#         1 2 3 4 5 6 
#           1 2 3 4 5 
#             1 2 3 4 
#               1 2 3 
#                 1 2 
#                   1 
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()
 
for i in range(10):
    # Print leading spaces
    for j in range(i+2):
        print (" ",end=" ")
    # Count down
    for j in range(1,9-i):
        print (j,end=" ")
    # Next row
    print()


# 13.
#                   1 
#                 1 2 1 
#               1 2 3 2 1 
#             1 2 3 4 3 2 1 
#           1 2 3 4 5 4 3 2 1 
#         1 2 3 4 5 6 5 4 3 2 1 
#       1 2 3 4 5 6 7 6 5 4 3 2 1 
#     1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 
#   1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 
#     1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 
#       1 2 3 4 5 6 7 6 5 4 3 2 1 
#         1 2 3 4 5 6 5 4 3 2 1 
#           1 2 3 4 5 4 3 2 1 
#             1 2 3 4 3 2 1 
#               1 2 3 2 1 
#                 1 2 1 
#                   1                  
for i in range(10):
    # Print leading spaces
    for j in range(10-i):
        print (" ",end=" ")
    # Count up
    for j in range(1,i+1):
        print (j,end=" ")
    # Count down
    for j in range(i-1,0,-1):
        print (j,end=" ")
    # Next row
    print()
 
for i in range(10):
    # Print leading spaces
    for j in range(i+2):
        print (" ",end=" ")
    # Count up
    for j in range(1,9-i):
        print (j,end=" ")
    # Count down
    for j in range(7-i,0,-1):
        print (j,end=" ")
    print()