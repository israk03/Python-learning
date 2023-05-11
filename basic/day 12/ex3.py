""" 
    string reversing

    input: "I Love Coding."
    output: "I evoL gnidoC."
"""

a = input("")
a = a.spit(" ")

print(a)

result = " "

for i in a: 
    result += i[ : :-1] + " "

print(result)