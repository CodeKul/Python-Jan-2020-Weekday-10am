'''
    if condition:
        true statements
    else:
        false statements
'''

a = 30
b = 20

# if a < b:
#     print('a is less than b')
# else:
#     print('a is greater than b')
#     print('this is inside else')

# if a < b:
#     print('a is less than b')
# elif a == b: 
#     print('a and b both are equal')
# else:
#     print('a is greater than b')

# if a < b:
#     print('a is less than b')
# else:
#     if a == b:
#         print('a and b both are equal')
#     else:
#         print('a is greater than b')


# Loops

'''
    while condition:
        statements
        incr/decr
'''
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         print('Codekul')
#     else:
#         print('The Gurukul for Coders!')
#     i += 1

# print(i)

'''
    for item in collection:
        statements
'''

# for ch in "Codekul":
#     print(ch)

sum = 0
for index, no in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print('Index:', index)
    print('Value:', no)
    sum += no

print(sum)