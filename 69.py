#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print("Please guess a letter: ")
guess = input()
lower_guess = guess.lower()
print(f'You guessed {lower_guess}')

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#via string: if guess in chosen_word:
#   print(f'Yes, the word contains {guess}')
#else:

#via list, less efficient
char_list = list(chosen_word)
for i in range(len(char_list)):
    print(i)
    print(len(char_list))
    print(f'checking letter {char_list[i]}')
    if char_list[i] == lower_guess:
        print(f'Yes, the word contains {guess}')
        break;
    elif i == len(char_list)-1:
        print(f'No, {guess} is not in word')
