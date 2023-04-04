""" integer number print in revers """

a = int(input())
rev = 0

while(a>0):
    last_digit = a % 10
    rev = rev*10 + last_digit
    a = a//10
print(rev)