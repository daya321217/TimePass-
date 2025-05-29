name = input("Type your name:")
print("Welcome", name, "to this adventure!!")

answer = input("your are on a dirt road and its come to an end and you can go left or right.\n where would you like to go?? Type 'left' or 'right': ").lower()

if answer == "left":
    answer = input("You come to a river, do you want to swim across or wait for a boat?\n Type 'swim' or 'wait': ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "wait":
        print("You waited for a boat and were rescued. You win!")
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to a bridge, do you want to cross it or go back?\n Type 'cross' or 'back': ").lower()
    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them or run away?\n Type 'talk' or 'run': ").lower()
        if answer == "talk":
            print("You talked to the stranger and they gave you treasure. You win!")
        elif answer == "run":
            print("You ran away safely, but missed out on the treasure. You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer == "back":
        print("You went back and got lost in the woods. You lose.")
    else:
        print("Not a valid option. You lose.")


else:
    print("Not a valid option. You lose.")
