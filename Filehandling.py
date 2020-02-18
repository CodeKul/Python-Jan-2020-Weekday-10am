'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

# f = open("abc.txt", "a")
# f.write(' - The Gurukul for Coders!')

f = open("abc.txt", "r")
# data = f.read()
# print(data)

# data = f.readline()
# print(data)

# data = f.readline()
# print(data)

# data = f.readlines()
# print(data)

# print("tell:", f.tell())

f.seek(3, 0)
data = f.readline()
print(data)

f.seek(3, 1)
data = f.readline()
print(data)