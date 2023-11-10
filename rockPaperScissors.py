import random


while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("Rock, Paper or Scissors?").lower()

    if player == computer:
        print("Tie")
        print("You chose:", player)
        print("Computer chose:", computer)

    elif player == "rock":
        if computer == "paper":
            print("You chose:", player)
            print("Computer chose:", computer)
            print("You lose")
        if computer == "scissors":
            print("You chose:", player)
            print("Computer chose:", computer)
            print("You win")
    elif player == "paper":
        if computer == "scissors":
            print("You chose:", player)
            print("Computer chose:", computer)
            print("You lose")
        if computer == "rock":
            print("You chose:", player)
            print("Computer chose:", computer)
            print("You win")
    elif player == "scissors":
        if computer == "rock":
            print("You chose:", player)
            print("Computer chose:", computer)
            print("You lose")
        if computer == "paper":
            print("You chose:", player)
            print("Computer chose:", computer)
            print("You win")

    playAgain = input("Would you like to play again? (yes/no): ").lower()

    if playAgain != "yes":
        break
print("Bye")