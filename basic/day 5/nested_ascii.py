""" print this with ASCII code:
            A                       A = 65 | a = 97
            B B                     B = 66 | b = 98
            C C C                   C = 67 | c = 99
            D D D D                 .        .
            E E E E E               .        . """

for row in range(5):
    for colum in range(row+1):
        print(chr(65 + row), end = " ")
    print()