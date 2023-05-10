# swaping two list elements:

a = [17,11,12,13,14,15,16,10]

temp = a[0]
a[0] = a[7]     # a[0] = a[-1] or a[len(a)-1]
a[7] = temp

print(a)