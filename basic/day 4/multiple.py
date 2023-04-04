""" you are given two integers, M and N.
u must chek whether M is an exact multiple of N,without using loops.
u have to output 0 if M is not a multiple of N.
u have to output M/N if M is multiple of N.
output u have to output 0 if M is not a multople of N. 
U have to output M/N if M is a multiple of N. """

M = int(input())
N = int(input())

if M%N==0:
    print(int(M/N))

else:
    print(0)
