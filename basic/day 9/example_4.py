# using if condition with list comprehension :

# long methode: 
a = []
for i in range(1,20):
    if i%3==0:
        a.append(i)
    if i%5==0:
        a.append(i)

print(a)

# using list comprehension :
b = [i for i in range(1,20) if i%3==0 or i%5==0]
print(b)