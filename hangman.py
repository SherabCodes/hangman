import random
import words from words
import string

def get_word(words):
  word = random.choice(words)
  while ' ' in word or '-' in word:
    word= random.choice(words)
  return word.upper()

def hangman():
  word = get_word(words)
  word_letters = set(word) #keeps track of the letters in the word
  alphabet = set(string.ascii_uppercase)
  used_letters = set() # Keeps track of what's already been guessed by the user

  while len(word_letters) > 0:

    print("The words you have guessed so far: ",' '.join(used_letters))

    word_list = [letter for letter in used_letters else '_' for letter in word]
    print("Your word: ", ' '.join(word_list))
    user_input = input("Guess a Letter: ").upper()
    if user_input in alphabet - used_letters: # Checks if the letter is valid and not previously guessed by the user
      used_letters.add(user_input)
      if user_input in word_letters:
        word_letters.remove(user_input)

    elif user_input in used_letters:
      print("You have guessed this letter previously! Try guessing a different letter")
    else:
      print("Enter a valid letter")

  




