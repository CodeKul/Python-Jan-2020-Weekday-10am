# -1 1 0 1 1 2 3 5 8 ...

a = -1
b = 1
c = 0
n = int(input("Enter a number: "))
while c < n:
    c = a + b
    print(c)
    a = b
    b = c