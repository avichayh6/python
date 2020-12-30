from random import randint
from time import sleep
print("this is game\neach turn cost 3$\n")
a=int(input("how much mony you have: "))
print("you have " + str(a//3) + " turns\nyour cheng is: " + str(a%3) + "\n")
prize=0

for x in range(a//3):
    print("turn number " + str(x+1) + "\n------------")
    cuba=randint(1,6)
    cubb=randint(1,6)
    print("cube a: " + str(cuba) + "\ncube b: " + str(cubb) + "\n")
    if (cuba==cubb):
        if (cuba==6):
            prize=prize+1000
        else:
            prize=prize+100
    elif (cuba==1):
        prize=prize+20
    elif (cubb==2):
        prize=prize+40
print("your prize: " + str(prize))