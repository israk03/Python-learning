# list theke 10 er nicher value print:

list =[12,34,9,7,6,34]
for i in list:
    if i<10:
        print(i)


# 3 and 5 dara divisible emn value:

for i in range(20):
    if i%3==0 and i%5==0:
        print(i)


# 1+2+3+4+5+.........

sum = 0
for i in range(1,11):
    sum = sum+i
print(sum)