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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0 , 2)
game_images = [rock, paper, scissors]
if choice >= 3 or choice < 0 :
  print("You typed an invalid number")
else:
  print(game_images[choice])
  
  if computer == 0:
    print(f"Computer chose:\n {rock}")
  elif computer == 1:
    print(f"Computer chose:\n {paper}")
  else: 
    print(f"Computer chose:\n {scissors}")
  
  if choice == computer:
    print("Its draw")
  elif choice == 0  and computer == 1:
    print("You lose")
  elif choice == 0 and computer == 2:
    print("You Win")
  elif choice == 1 and computer == 2:
    print("You Lose")
  elif choice == 1 and computer == 0:
    print("You Win")
  elif choice == 2 and computer == 0:
    print("You Lose")
  elif choice == 2 and computer == 1:
    print("You Win")
  

