def my_function():
    print('This is my function')

my_function()

def function_with(myVar1, myVar2, myVar3='CODEKUL'):
    print('This is my myVar1:', myVar1)
    print('This is my myVar2:', myVar2)
    print('This is my myVar3:', myVar3)

a = 12.43
b = 100
c = 'ABCD'
function_with(myVar2=10, myVar1=11.22)

def function_returning():
    s1 = "Codekul"
    return s1

print(function_returning())


def change_var(var1):
    var1 = 100
    print('var1:', var1)

var = 10
change_var(var)
print('var:', var)

def change_list(l1):
    l1 = [1,2,3,4,5,6]
    print('l1:', l1)

l = [1,2,3,4,5]
change_list(l)
print('l:', l)