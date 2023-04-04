""" you will be given 3 integers as input.
the inputs may or may not be different fron each other.
you have to output 1 if all three inputs are different from each other.
and 0 if any input is repeated more than once.
 """

a = int(input())
b = int(input())
c = int(input())

if (a!=b and a!=c and b!=c):
                          print(1)

else:
   print(0)