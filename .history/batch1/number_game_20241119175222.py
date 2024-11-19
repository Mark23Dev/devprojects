import random

def computer_choice():
    choice = random.randint(1,10)
    return choice

class Play:
    def __init__(self, guess, guess_number):
        self.guess = guess
        self.guess_number = guess_number

    def player_guess(self):
        self.guess 
