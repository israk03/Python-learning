age = int(input("What is your age?"))

if age >= 18:
    nationality = input("Do you have NID card? (y/n)")
    if nationality == 'y':
        vapelicense = input("Do you have vapelicense? (y/n)")
        if vapelicense == 'y':
            print("Congratulations, you can buy this vape.")
        else:
            print("You must have the license.")
    else:
        print("You must have your NID.")
else:
    print("You are too young.")