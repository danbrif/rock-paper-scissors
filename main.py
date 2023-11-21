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

# Code starts below 👇
game_img = [rock, paper, scissors]

yours = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if yours >= 3 or yours < 0:
  print("You typed invalid number. You lose.")
else:
  print(game_img[yours])

  import random
  computer = random.randint(0, 2)
  print(f"Computer chose:\n {game_img[computer]}")
  
  if yours == computer:
    print("It's a draw. Try more!")
  elif yours == 0 and computer == 2:
    print("You win!")
  elif computer == 0 and yours == 2:
    print("You lose.")
  elif computer > yours:
    print("You lose.")
  else:
    print("You win!")
# End of code
