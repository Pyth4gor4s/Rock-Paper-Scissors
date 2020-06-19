#!/usr/bin/env python3
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()


"""
This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round.
The game has 4 different players:
- A player that always plays 'rock'
- A player that chooses its moves randomly
- A player that remembers and imitates what the human player
did in the previous round.
- A player that cycles through the three moves
"""

moves = ['rock', 'paper', 'scissors']


class Player:
    """
    The Player class is the parent class for all of the Players
    in this game

    Attributes
    ----------
    my_move : str
    their_move : str

    Methods
    -------
    move(self)
        Prints the moves of the player depending on the
        players strategy
    learn(self, my_move, their_move)
        Used in the Player-Subclass Reflect Player to imitate
        what the human player did in the previous round
    """

    my_move = None
    their_move = None

    def move(self):
        """Returns the moves of the player from the moves list
        depending on the players strategy"""
        return moves[0]

    def learn(self, my_move, their_move):
        """Used in the Player-Subclass Reflect Player to imitate
        what the human player did in the previous round
        Here it just passes

        Parameters
        ----------
        my_move : str
            The move of the first player
        their_move : str
            The move of the second player
        """
        pass


def beats(one, two):
    """Keep score, tell whether one move beats another one

    Parameters
    ----------
    one : str
        A move that depends on the player.
    two: str
        Another move that depends on the player.
    """
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    """Player-Subclass for a player that chooses
    its moves randomly'"""
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    """Player-Subclass for a human player"""
    def move(self):
        while True:
            self.human_input = input("Rock, paper, "
                                     "scissors? > ").lower()
            if self.human_input in moves:
                return self.human_input
            else:
                print("Sorry, that's no valid input")


class ReflectPlayer(Player):
    """Player-Subclass that remembers and imitates what the human player
    did in the previous round."""
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    """Player-Subclass that that cycles through the three moves"""
    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
            return self.my_move
        elif self.my_move == 'rock':
            self.my_move = 'paper'
            return self.my_move
        elif self.my_move == 'paper':
            self.my_move = 'scissors'
            return self.my_move
        else:
            self.my_move = 'rock'
            return self.my_move


class Game:
    """
    Class to initialise and play the game.

    Attributes
    ----------
    p1 : str
        Player 1 of the game
    p2 : str
        Player 2 of the game
    p1_score : int
        Initial score of player 1
    p2_score : int
        Initial score of player 2

    Methods
    -------
    play_round(self)
        Play a round of the game
    play_again(self)
        Play the whole game again after game over
    play_game(self)
        Start and play the game
    """

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
        print()

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
        number_of_rounds = 3
        for round_number in range(number_of_rounds):
            print(Fore.GREEN + f"Round {round_number}:" + Style.RESET_ALL)
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
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
