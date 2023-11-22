import random

print("Welcome to the Number guessing game!")

def guess():
    random_number = random.randint(1, 100)
    print(random_number)  # You can remove or comment out this line for the final version
    attempts_left = 3

    while attempts_left > 0:
        print("Please guess any number between 1 to 100")
        num = int(input())

        if num == random_number:
            print("Congratulations! You won.")
            break
        elif num > random_number:
            print("Your guessed number is greater than the actual number.")
        else:
            print("Your guessed number is lower than the actual number.")

        attempts_left -= 1
        print("You have", attempts_left, "attempt(s) left.")

# Initial guess
guess()
n
while True:
    choice = input("Do you want to continue? (Y/N)").lower()

    if choice == 'y':
        guess()
    elif choice == 'n':
        print("Thank you for playing.")
        break
    else:
        print("Invalid choice. Please enter 'Y' or 'N'.")
