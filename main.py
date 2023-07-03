from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too High.\nGuess again.")
    return turns - 1
  elif guess < answer:
    print("Too Low.\nGuess again")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")
#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
    
def game():
#Choosing a random number between 1 and 100.
  print(logo)
  print("\nWelcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1,100)
  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"\nYou have {turns} attempts remaining to guess the number.")
  #Let the user guess a number.
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
  #Track the number of turns and reduce by 1 if they get it wrong.
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return      


game()