""" print 1st 20 fibonacci series """

a, b = 0, 1
x = int(input())

for i in range(1, x+1):
    
    result = a+b
    a = b
    b = result

    print(a, end = " ")