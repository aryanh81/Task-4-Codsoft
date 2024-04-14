import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

def winner():
    global player_score, computer_score
    if player_score > computer_score:
        print("You Won")
    elif computer_score > player_score:
        print("Computer Won")
    else:
        print("Tied")

def score(player, computer):
    global player_score, computer_score
    if player == computer:
        pass
    elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        player_score += 1
    else:
        computer_score += 1

def main():
    global player_score, computer_score
    while True:
        player = int(input("(1)Rock/ (2)Paper/ (3)Scissors/ (4)Exit: "))
        if player == 4:
            winner()
            break
        elif player not in [1, 2, 3, 4]:
            print("Invalid choice. Try again")
            continue
        else:
            player = choices[player - 1]

            computer = random.choice(choices)

            print(f"You: {player}, Computer: {computer}")
            score(player, computer)
            print("SCORE:")
            print(f"You: {player_score} VS Computer: {computer_score}")


main()
