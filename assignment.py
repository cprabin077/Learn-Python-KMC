import random

# Rock , Scissors, Papers -> Games
games_data = ["r", "p", "s"]
data = random.choice(games_data)
print(data)
user_score = 0
computer_score = 0

while True:
    user_data = input("Enter r, p, s or 'quit' to exit: ").lower()

    if user_data == "quit":
        print("Final Score -> You:", user_score, "Computer:", computer_score)
        break

    if user_data not in games_data:
        print("Invalid choice! Try again.")
        continue

    if user_data == data:
        print("Game Draw!!")
    elif (
        user_data == "r"
        and data == "s"
        or user_data == "p"
        and data == "r"
        or user_data == "s"
        and data == "p"
    ):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

