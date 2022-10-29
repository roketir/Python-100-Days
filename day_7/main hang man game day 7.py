import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
print()
print('You have 6 life for worng answers !')
print()

chosen_word = random.choice(word_list)
lives = 6

#Testing code
#print(f'The solution is {chosen_word}.')

#Creating the game template 
display = []
for letter in chosen_word :
    display.append('_')


while '_' in display:
    guess = input("Guess a letter: ").lower()
    
    clear()
    
    if guess in display:
        print(f"A letteer '{guess}' alredy guessed ! ")

    index = 0
    if guess not in chosen_word:
        lives -=1
        print(stages[lives])
        print(f"A letteer '{guess}' is not in the word, you lose a life your corrent life is '{lives}' try again ! ")
        print()
    for letter in chosen_word:
        if letter == guess:
            display[index]=letter
            index +=1
        else:
            index +=1
        
    print(display)
    print()

    if lives == 0:
        break

if lives == 0:
    print(stages[0])
    print('Game Over, You lost !!!')
else:
    print('You won !!!')

