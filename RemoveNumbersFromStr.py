# input: Codekul-Python-10am-11am-2020
# output:Codekul-Python-am-am-

s1 = input("Enter a string: ")

def removeNo(str1):
    i = 0
    while i < len(str1):
        if str1[i].isdigit():
            str1 = str1.replace(s1[i], "", 1)
        else:
            i += 1
    return str1

print('Output: ',removeNo(s1))