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

game = [rock,paper,scissors]

user = int(input("Choice your move 0 - Rock, 1 - Paper, 2 - Scissors\n"))

if user > 3 and user <= 0:
    print("You typed an invalide number, You loss!")
else:
    print(f"User Choice {user} :")
    print(game[user])
    computer = random.randint(0,2)
    print(f"Computer Choice {computer} :")
    print(game[computer])

    if user == 0 and computer == 2:
        print("You Win!")
    elif user == 1 and computer == 0:
        print("You Win!")
    elif user == 2 and computer == 1:
        print("You Win!")
    elif user == 0 and computer == 1:
        print("You Loss!")
    elif user == 1 and computer == 2:
        print("You Loss!")
    elif user == 2 and computer == 0:
        print("You Loss!")
    elif user == 0 and computer == 0:
        print("Game Draw!")
    elif user == 2 and computer == 2:
        print("Game Draw!")
    elif user == 1 and computer == 1:
        print("Game Draw!")
