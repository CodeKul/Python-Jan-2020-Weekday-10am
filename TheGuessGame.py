import random

while True:
    r_no = random.randint(1, 10)
    u_no = int(input('Enter a number between 1-10: '))

    if r_no == u_no:
        print('You won!')
    else:
        print('Better luck next time!')
    opt = input('Do you want to continue? y/n: ')
    if opt == 'y':
        continue
    else:
        break
print('Bye...')