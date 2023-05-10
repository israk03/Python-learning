#           [if else for i in list]

# if else with list comprehension:

# noob:
a = []
for i in range(20):
    if i%2==0:
        a.append("even")
    else:
        a.append("odd")
print(a)

# pro:
b = ["even" if i%2==0 else "odd" for i in range(20)]
print(b)