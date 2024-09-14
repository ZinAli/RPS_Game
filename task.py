import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



user_choose = int(input("hat do you choose? type 0 for Rock, 1 for Paper or 2 for scissors"))
game = [rock,paper,scissors]


if user_choose >= 3 or user_choose < 0:
    print("Wrong choice!")
else:
    print("Your choose:" + game[user_choose] + "\n")

computer_choose = random.randint(0,2)
print(computer_choose)
print("Computer choose:" + game[computer_choose] + "\n")


if user_choose >= 3 or user_choose <0:
    print("Invalid choice")
elif user_choose == computer_choose:
    print("It's a draw")
elif (user_choose == 0 and computer_choose == 2) or (user_choose == 1 and computer_choose == 0) or (user_choose == 2 and computer_choose ==1):
    print("You win!")
else:
    print("You loose")

