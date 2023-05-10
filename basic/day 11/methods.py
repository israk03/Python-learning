a = "HElLo wOrLD"

# converts character into lowercase:
b = a.lower()   # print(a.casefold())
print(b)

# converts character into uppercase: 
c = a.upper()
print(c)

# converts string to title case:
d = a.title()
print(d)

# capitalize:
e = a.capitalize()
print(e)

# swapcase:
f = a.swapcase()
print(f)

# replace: 
g = "helle"
h = g.replace(b[4], "o")
print(h)

# count: 
i = a.count("l")
print(i)

# join:
j = ["h", "e", "l", "l", "o"]
print("".join(j))