import random

class Game:
    @staticmethod
    def computer_choice():
        choice = random.randint(1,10)
        return choice

class Play(Game):
    def __init__(self):
        self.guess = ''
        self.guess_number = 0

    def player_move(self):
        while self.guess_number < 3:
            self.guess = int(input(f"Guess: "))
            self.guess_number += 1
            if self.guess == super().computer_choice():
                print("You win!")
                break
            else:
                print("Try again")
        else:
            print("You lose!")

game_play = Play()
game_play.player_move()