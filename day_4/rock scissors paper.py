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
print('-' * 40)
print('-' * 5 + 'Wlcome To Rock Scissors Paper ' + '-' * 5)
print('-' * 40)
print()
import random

user_choice = int(input('Please enter your choice: " 1 for Rock, 2 for Paper, 3 for  Scissors " -  '))
computer_choice = random.randint(1, 3)

if user_choice == 1:
  print(rock)
elif user_choice == 2:
  print(paper)
elif user_choice == 3:
  print(scissors)
else:
  print('--------------------------------')
  print('You enterd not a valide number !')
  print('--------------------------------')

print('The computer choce is :')

if computer_choice == 1:
    print(rock)
elif computer_choice == 2:
  print(paper)
elif computer_choice == 3:
  print(scissors)
  
if user_choice == computer_choice:
  print('Its tay try again!')
elif user_choice == 1 and computer_choice == 2:
  print('Computer Win !')
elif user_choice == 1 and computer_choice == 3:
  print('You Win !')
elif user_choice == 2 and computer_choice == 1:
  print('You Win !')
elif user_choice == 2 and computer_choice == 3:
  print('Computer Win !')
elif user_choice == 3 and computer_choice == 1:
  print('Computer Win !')
elif user_choice == 3 and computer_choice == 2:
  print('You Win !')
else:
  print('Game Over')