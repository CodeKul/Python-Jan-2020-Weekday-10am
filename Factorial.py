def calc_factorial(no):
    fact = 1
    while(no > 1):
        fact *= no
        no -= 1
    return fact

no = int(input('Enter a number: '))
fact = calc_factorial(no)

print('Factorial of {}: {}'.format(no, fact))