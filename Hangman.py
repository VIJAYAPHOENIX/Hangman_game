from replit import clear
import random
from Handman_art import logo,stages
from Hangman_words import topics
lives = 6
filled_blanks=0
end_point = False
print(logo)
chosen_topic = random.choice(list(topics.keys()))
print(f"selected topic is {chosen_topic}")
chosen_word = random.choice(topics[chosen_topic])
display = []
count=0
for slash in chosen_word:
    display.append("_")
    count+=1
print(display)
while not end_point:
    guess = input("make your choice :- ").lower()
    clear()
    if guess in display:
            print("already guessed this word")
    correct_guess = False
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position]=letter  
            correct_guess = True
    if correct_guess == False:
        lives = lives-1
        print("Oops it's a wrong guess")
        if lives == 0:
            print("Game over my friend")
            end_point = True
    if "_" not in display:
        end_point = True
        print("well done ,You win")
    print(display)
    print(stages[lives])
    print(f"Remaining life lines are {lives}")