""" python program to print a multiplication table(namta) of a given number:
        5 X 1 = 5
        5 X 2 = 10
        5 X 3 = 15
        .
        .
        .
        5 X 10 = 50 """

a = int(input())
for i in range(1,11):
    print(a, " X ",i, "=", a*i)