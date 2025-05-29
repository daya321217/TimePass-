import random

def get_top_of_range():
    while True:
        top_of_range = input("Type a number greater than 0: ")
        if top_of_range.isdigit():
            top_of_range = int(top_of_range)
            if top_of_range > 0:
                return top_of_range
            else:
                print("Please type a number larger than 0.")
        else:
            print("Please type a valid number.")

def get_user_guess():
    while True:
        user_guess = input("Make a guess: ")
        if user_guess.isdigit():
            return int(user_guess)
        else:
            print("Please type a valid number.")

def main():
    guesses = 0
    top_of_range = get_top_of_range()
    random_number = random.randint(0, top_of_range)

    while True:
        guesses += 1
        user_guess = get_user_guess()

        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    print(f"You got it in {guesses} guesses.")

if __name__ == "__main__":
    main()
