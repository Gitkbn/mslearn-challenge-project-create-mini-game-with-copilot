# write "hello.world" to the console
print("hello world")

# Get one of three options rock, paper, or scissors from the user
user_choice = input("rock, paper, or scissors? ")

# Print the user's choice
print("User's choice: ", user_choice)

# Get a random choice from the computer
import random
computer_choice = random.choice(["rock", "paper", "scissors"])

# Print the computer's choice
print("Computer's choice: ", computer_choice)

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":

    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose!")  

elif user_choice == "paper":

    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")

elif user_choice == "scissors":

    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")

else:
    print("Invalid choice")     


# Loop to play again
    
while True:

    play_again = input("Do you want to play again? (yes/no) ")
    if play_again == "yes":
        user_choice = input("rock, paper, or scissors? ")
        print("User's choice: ", user_choice)
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print("Computer's choice: ", computer_choice)
        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("You win!")
            else:
                print("You lose!")  
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
            else:
                print("You lose!")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("You win!")
            else:
                print("You lose!")
        else:
            print("Invalid choice") 
    else:
        break
