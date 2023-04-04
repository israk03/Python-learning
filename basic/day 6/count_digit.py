""" count thr number of digit in a number """

# method: 1
a = int(input())
count = 0
while (a>0):
    digit = a % 10          # eta diye num er last digit ta peye jai. use na korleo hoito
    count += 1
    a = a // 10             # integer division diye last digit bad kora jay

print(count)

# method: 2

print(len(a))