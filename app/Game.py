import random


class Game:
    def __init__(self):
        self.validPlays = ["rock", "paper", "scissors"]
        self.playerPlay = None
        self.computerPlay = None
        self.continuePlay = "yes"
        self.winner = None

    def makePlay(self) -> str:
        self.computerPlay = random.choice(self.validPlays)
        self.playerPlay = None

        while self.playerPlay not in self.validPlays:
            print("Choose One\n Rock, Paper, Scissors: ")
            self.playerPlay = input().lower()
    
    def checkWinner(self) -> str:
        if self.computerPlay == self.playerPlay:
            return "Draw"

        elif self.computerPlay == "rock":
            return "Computer" if self.playerPlay == "scissors" else "Player"

        elif self.computerPlay == "paper":
            return "Computer" if self.playerPlay == "rock" else "Player"
        
        elif self.computerPlay == "scissors":
            return "Computer" if self.playerPlay == "paper" else "Player"

    def run(self):
        print("Welcome")

        while self.continuePlay == "yes":
            self.makePlay()
            self.winner = self.checkWinner()
            print(f"\nPlayer: {self.playerPlay}\nComputer: {self.computerPlay}")
            print("Draw") if self.winner == "Draw" else print(f"{self.winner} won!")
            print("Do you want to play again? (yes/no): ")

            self.continuePlay = input().lower()