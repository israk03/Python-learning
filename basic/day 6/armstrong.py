""" python program to check Armstrong number. """

a = int(input())
num_len = len(str(a))
temp = a
sum = 0

while(a>0):
    last_digit = temp % 10
    sum = sum + last_digit**num_len
    temp = temp // 10

if (sum == a):
    print("Armstrong.")
else:
    print("Not Armstrong.")

    # problem asey