""" python program to find the factorial of a given number.
        5! = 1*2*3*4*5 = """

a = int(input())
fact = 1                # multiplication korbo tai storage e 1 rekhechi
for i in range(1, a+1):
    fact = fact*i
print(fact)