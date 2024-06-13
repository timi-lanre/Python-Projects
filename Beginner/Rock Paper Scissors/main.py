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


user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu = random.randint(0,2)

if user == 0: 
  print(rock+"\n")
  print("Computer chose:\n")
  if cpu == 0:
    print(rock+"\n")
    print("You tie.")
  elif cpu == 1:
    print(paper+"\n")
    print("You lose.")
  else:
    print(scissors+"\n")
    print("You win.")
elif user == 1:
  print(paper+"\n")
  print("Computer chose:\n")
  if cpu == 0:
    print(rock+"\n")
    print("You win.")
  elif cpu == 1:
    print(paper+"\n")
    print("You tie.")
  else:
    print(scissors+"\n")
    print("You lose.")
else:
  print(scissors+"\n")
  print("Computer chose:\n")
  if cpu == 0:
    print(rock+"\n")
    print("You lose.")
  elif cpu == 1:
    print(paper+"\n")
    print("You win.")
  else:
    print(scissors+"\n")
    print("You tie.")
  