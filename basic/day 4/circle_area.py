import math

rad = float(input("please enter the area of circle: "))

if rad>0:
    area = math.pi * rad * rad
    print("the area of circle is", area)
else:
    print("can't find the area.")