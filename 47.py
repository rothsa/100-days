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
import string
import secrets
#Write your code below this line 👇
print("Let's Play rock, paper, scissors!")

print ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors and hit enter. Any other entry will exit the game.")

choice = 0
display = [rock, paper, scissors]
while choice in range(0, 3):
    computer_choice = secrets.randbelow(3)
    raw_choice = input()
    if raw_choice not in ["0","1","2"]:
        print("That's it! Good game.")  
        break;
    choice = int(raw_choice)
    print("Computer choice: " + display[computer_choice] + "\nYour choice: " + display[choice])
    if computer_choice == choice:
       print("It's a tie!")
    elif [computer_choice, choice] in [[0,1],[1,2],[2,0]]:
       print("You win!")
    else:
       print("Computer wins!")
else:
    print("That's it! Good game.")   
    
