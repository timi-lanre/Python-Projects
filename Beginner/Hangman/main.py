import random
from hangman_art import logo, stages
from hangman_words import word_list

def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos


#start of the game 
print(logo)



guess_limit = 7 
guessed_word= random.choice(word_list)



len_guessed = int(len(guessed_word))
placeholder = "_" * len_guessed



end_check = '_'


index = 0 
while guess_limit > 0:
  guess = input("Guess a letter:\n").lower()
  if guess in guessed_word: 
    pos_x = charposition(guessed_word, guess)
    for i in pos_x:
        placeholder = placeholder[:i] + guess + placeholder[i+1:]
        print(placeholder)
  else:
    guess_limit -= 1
    print(stages[guess_limit])
    print(placeholder)
  if end_check not in placeholder:
           print("You Win")
           exit()

if guess_limit == 0: 
  print("You Lose")
  print(f"The word is {guessed_word}")
    
    






