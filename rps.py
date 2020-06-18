#!/usr/bin/env python3
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    my_move = None
    their_move = None

    def move(self):
        return moves[0]

    def learn(self, my_move, their_move):
        pass


""" Keep score, tell whether one move beats another one: """


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


""" Subclass of the Player class, to play moves randomly': """


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


""" Subclass for a human player: """


class HumanPlayer(Player):
    def move(self):
        while True:
            self.human_input = input("Rock, paper, "
                                     "scissors? > ").lower()
            if self.human_input == 'rock':
                return ('rock')
                break
            elif self.human_input == 'paper':
                return('paper')
                break
            elif self.human_input == 'scissors':
                return('scissors')
                break
            else:
                print("Sorry, that's no valid input")


""" Player-Subclass that remembers what move the opponent played
last round and plays that move this round: """


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


""" Player-Subclass that always plays the opponent,
based on the choice of the humand player: """


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(Back.CYAN + "Player 1: " + Style.RESET_ALL + f"{move1}  "
              + Back.RED + "Player 2: " + Style.RESET_ALL + f"{move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        # if-else statement to keep score:
        if beats(move1, move2):
            self.p1_score += 1
        elif beats(move2, move1):  # when move2 is first
            self.p2_score += 1
        else:
            print("Tie!")

        print("Score: " + Fore.CYAN + f"Player One {self.p1_score}, "
              + Style.RESET_ALL + Fore.RED + "Player Two "
              f"{self.p2_score}" + Style.RESET_ALL)

    def play_again(self):
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "n":
            print("Ok. Goodbye!")
        elif play_again == "y":
            print("Yeah! Let's play again!")
            self.p1_score = 0
            self.p2_score = 0
            game.play_game()
        else:
            ("Sorry, that's no valid input. Please type 'y' or 'n'")

    def play_game(self):
        print(Fore.RED + "Game start!\n" + Style.RESET_ALL)
        for round in range(3):
            print(Fore.GREEN + f"Round {round}:" + Style.RESET_ALL)
            self.play_round()
        if self.p1_score == self.p2_score:
            print("It's a tie!")
        elif self.p1_score > self.p2_score:
            print("Player 1 wins the game!")
        else:
            print("Player 2 wins the game!")
        print("Game over!")
        game.play_again()


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
