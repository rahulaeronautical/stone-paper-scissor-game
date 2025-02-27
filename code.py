import random

while True:
    user_action = str(input("Enter a choice (rock, paper, scissors): ")).lower()
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    massage=""

    if user_action == computer_action:
        massage=f"Both players selected {user_action}. It's a tie!"
    elif user_action == "rock":
        if computer_action == "scissors":
           massage= "Rock smashes scissors! You win!"
        else:
            massage="Paper covers rock! You lose."
    elif user_action == "paper":
        if computer_action == "rock":
            massage="Paper covers rock! You win!"
        else:
            massage="Scissors cuts paper! You lose."
    elif user_action == "scissors":
        if computer_action == "paper":
            massage="Scissors cuts paper! You win!"
        else:
            massage="Rock smashes scissors! You lose."
    else:
         print ("you entered a wrong value")
         continue
    print(f"\nYou choose {user_action}, computer choose {computer_action}.\n") 
    print(massage)  

    play_again = str(input("Play again? (y/n): "))
    if play_again.lower() != "y":
        break
print("Thank you for playing")