# for loop:

for i in range(10):
    print(i)
    if i ==5:            # ekhane 5 o print korbe cz if er condition last e deya and last e cheaq korbe.
        continue


for i in range(10):
    if i == 5:          # ekhane  5 skip korbe
        continue
    print(i)



# while loop:

a = 10 
while a<=10:
    a = a+1 
    if a ==5:
        continue
    print(a)