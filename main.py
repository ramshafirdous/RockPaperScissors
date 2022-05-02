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

#Write your code below this line 👇
import random

image_list= [rock, paper, scissors]

choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice >= 3 or choice < 0:
  print("invalid number, you lose")
else:
  print(image_list[choice])

  computer_choice= random.randint(0,2)
  print("Computer chose:" + image_list[computer_choice])

  if (choice==0 and computer_choice==2): 
    print("You win")
  elif (choice==2 and computer_choice==0):
    print("You lose")
  elif choice > computer_choice:
    print("You win")
  elif computer_choice > choice:
    print("You lose")
  elif choice==computer_choice:
    print("It's a draw")





