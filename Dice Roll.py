# Dan's D20 Random Roll
import time
import random


def dice():
    print("Would you like to roll the dice? ")
    response = input("Type Yes or No: ")
    if response == "YES" or "Yes" or "yes":
        print("Rolling dice now...")
        time.sleep(2)
        print("Visualize a dice rolling...")
        time.sleep(2)
        print("And...")
        time.sleep(1)
        result = random.randint(1,20)
        print(result)
    elif response == "NO" or "No" or "no":
        print("No roll today, sorry to hear.")
    else:
        print("You didn't type Yes or No, please try again.")
        dice()


dice()

# End
