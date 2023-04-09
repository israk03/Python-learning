a = [12,23,3.5,"alu"]

for i in a:             # list er value alada alada kore print korbe
    print(i)


# by using positive indexing:
for i in range(len(a)):
    print(a[i])

for i in range(len(a)-1, -1, -1):           # list er value reverse order e print korbe
    print(a[i])
    

# by using negative indexing:
for i in range(-1, -len(a)-1, -1):          
    print(a[i])