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

playerChoice = (input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
playerChoice = int(playerChoice)
if playerChoice == 0:
    print(rock)
elif playerChoice == 1:
    print(paper)
elif playerChoice == 2:
    print(scissors)
else:
    print("No")
cpuChoice = random.randint(0, 2)
print("CPU chose:")
if cpuChoice == 0:
    print(rock)
elif cpuChoice == 1:
    print(paper)
elif cpuChoice == 2:
    print(scissors)
else:
    print("No")

if playerChoice == 0 and cpuChoice == 2:
    print("You win!")
elif playerChoice == 0 and cpuChoice == 1:
    print("You lose")
elif playerChoice == 1 and cpuChoice == 0:
    print("You win!")
elif playerChoice == 1 and cpuChoice == 2:
    print("You lose")
elif playerChoice == 2 and cpuChoice == 1:
    print("You win!")
elif playerChoice == 2 and cpuChoice == 0:
    print("You lose")
else:
    print("Draw")
