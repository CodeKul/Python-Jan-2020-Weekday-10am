# str
str1 = "Codekul"
print(str1)
print(type(str1))
str2 = 'The Gurukul for Coders!'
print(str2)
print(type(str2))

# 'Codekul' - "The Gurukul for Coders"!

'''
    This is
    Multiline
    Comment
'''

print("""'Codekul' - "The Gurukul for Coders"!""")

str3 = '''Codekul

    The Gurukul for Coders!'''

print(str3)

str4 = str1 + " - " + str2
print(str4)

a = 10

# str5 = str1 + a

str5 = str1 + ' - {} - {}'.format(str2, a)

print(str5)

print(str1 + ' - %d'% a)
print(str1 + ' - %s'% str2)

print(str5.replace(' ', '_'))

# List

list1 = [1,2,3,4,5, 6.7, 'Eight', True]
list1[6] = 8

list1.append(10)
list1.reverse()
print(list1)
print(list1.index(6.7))

list2 = [1,2,3,4] + list1
print(list2)

list3 = [list1, list2]

print(list3)

# Dictionary

d1 = {'key1': 'value1', 'key2': 'value2'}
print(d1['key2'])

d2 = {1: 'One', 2: 'Two', 3: 'Three', 'Four': 4, 'Five': 5}

print(d2['Four'])

d3 = {'name': 'Varun', 'address': 'Pune', 'phone': '1234567890'}

d4 = {'name': 'Rajesh', 'address': 'Mumbai', 'phone': '0987654321'}

l1 = [d3, d4]

print(l1[1]['address'])

# Tuple

t1 = (1,2,3,4, 5.6, 'Seven', True)

t1.append(1)
t1[3] = 12

print(t1[3])