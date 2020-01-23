def addition(a, b):
    res = a + b
    return res

def subtraction(a, b):
    res = a - b
    return res

def multiplication(a, b):
    res = a * b
    return res

def division(a, b):
    res = a / b
    return res


a = int(input('Enter a number: '))
b = int(input('Enter aother number: '))
print(addition(a, b))
print(subtraction(a, b))
print(multiplication(a, b))
print(division(a, b))
