import random
import time
random_number=random.randint(1,50)
guess_right=5
while True:
    x=int(input("guess a number:"))
    if (random_number<x):
        print("..........")
        time.sleep(1)
        print("say low number")
        guess_right-=1
    elif(random_number>x):
        print("..........")
        time.sleep(1)
        print("say high number")
        guess_right-=1
    else:
        print("..........")
        time.sleep(2)
        print("congratulation corret guess corret:",random_number)
        break
    if (guess_right==0):
        print(("........."))
        time.sleep(1)
        print("your guess right finished")
        break


