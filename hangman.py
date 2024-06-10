import random
from jake import jake
import string

def get_valid_word(jake):
    word = random.choice(jake)
    while '-' in word or ' ' in word:
        word = random.choice(jake)

       

def hangman():
    word = get_valid_word(jake)
    word_letters = set()
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
   
    

    lives = 7

    while len(word_letters) > 0 and lives > 0:
      print('You have ', lives,'You have used these letters: ', ' '.join(used_letters))
      
    word_list= [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            
        else:
            lives = lives - 1 
            print('Letter is not in word. Try again')

    elif user_letter in used_letters:
        print('You have already used that letter. Try again')

    else:
        print('Invalid character. Please try again.')

    if lives == 0:
     print('You died, sorry. The word was',word)
    else:
      print(' You guessed the word',word,'!!')

hangman()