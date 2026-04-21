import random

# print(random.random()) # random value between 0 and 1

# print(random.random()*100) # random value between 0 and 1 * 100

# print(random.randint(10,20)) # random number between 10 and 20

# a = ["hello", "yes", "test", "namaste"]
# print(random.choice(a)) # print random value from the list


# number guessing
# guess_number = random.randint(10,40)
# num = int(input("Enter the number between 10 and 40: "))
# while(num != guess_number):
#     print("Wrong number!!")
#     num = int(input("Enter the number between 10 and 40: "))
# print("Number matched")


# another method of guessing number
# count = 0
# guess_number = random.randint(10,40)
# print(guess_number)
# while(True):
#     num = input("Enter the number between 10 and 40: ")
#     count = count + 1
#     if num == str(guess_number):
#         print(f"Number matched at {count} times")
#         play = str(input("Do you want to play more?? (y/n): ")).lower()
#         if(play == "y"):
#             guess_number = random.randint(10,40)
#             print(guess_number)
#             count = 0
#         else:
#             print("Thanks for playing")
#             break
#     else:
#         print("Try again!!")


# attempt wala questions -> assignment
# count = 5
# guess_number = random.randint(10,40)
# print(guess_number)
# while(count > 0):
#     num = int(input("Enter the number between 10 and 40: "))
#     count = count - 1
#     if num == guess_number:
#         print("Number matched:")
#         break
#     else:
#         print(f"You have {count} attempts left!!")
#         if count == 0:
#             print(f"You have finished your attempts and the generated random number is {guess_number}")


# User vs Computer game -> assignment
count_user = 0
count_computer = 0
guess_number = random.randint(1,5)
print(guess_number)
while(True):
    num = int(input("Enter the number: "))
    if num == guess_number:
        count_user += 1
    else:
        count_computer += 1

    if count_user == 5:
        print("Hurrah!! You won")
        break
    if count_computer == 5:
        print("Computer won!!")
        break

# rock, paper, scissors -> assignment
# games_data = ["r", "p", "s"]
# data = random.choice(games_data)
# print(data)

# while True:
#     user_data = input("Enter your choices (r,p,s): ").lower()
#     if user_data not in games_data:
#         print("Invalid choice: ")
#         continue
#     if data == user_data:
#         print("Game Draw")
#     elif (
#         user_data == "r"
#         and data == "s"
#         or user_data == "s"
#         and data == "p"
#         or user_data == "p"
#         and data == "r"
#     ):
#         print("You won!!")
#         break
#     else:
#         print("You loose!!")
        
