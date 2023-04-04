""" print this:
            #
            # #
            # # # 
            # # # #
            # # # # # """

for row in range(6):
    for colum in range(row):
        print("#", end = " ")
    print()
