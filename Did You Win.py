def game(match):
    win = input("Yes or No: ")
    if win == "Yes":
        print("Fuck Yea")
    elif win == "No":
        print("Fuck Me")
    else:
        print("Well did you win or not?")
        game()
game()