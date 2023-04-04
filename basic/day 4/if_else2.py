sub1 = int(input("Enter your sub1 marks: "))
sub2 = int(input("Enter your sub2 marks: "))
sub3 = int(input("Enter your sub3 marks: "))

avg = (sub1+sub2+sub3)/3

print("Your avarage marks is",avg)

if avg>90:
    print("Grade A.")
elif 80<=avg<=90:
    print("Grade B.")
elif 70<=avg<=80:
    print("Grade C.")
elif 60<=avg<=70:
    print("Grade D.")
else:
    print("F")