import random

def printPlay() -> str:
    print("Choose One\n Rock, Paper, Scissors: ")
    play = input().lower()
    return play

def checkWinner(computerPlay, playerPlay) -> str:
    if computerPlay == playerPlay:
        return "Draw"

    elif computerPlay == "rock":
        return "Computer" if playerPlay == "scissors" else "Player"

    elif computerPlay == "paper":
        return "Computer" if playerPlay == "rock" else "Player"
    
    elif computerPlay == "scissors":
        return "Computer" if playerPlay == "paper" else "Player"



def main() -> None:
    validPlays = ["rock","paper", "scissors"]
    continuePlay = "yes"

    print("Welcome")

    while continuePlay == "yes":
        play = None
        print("Let's play!\n")

        while play not in validPlays:
            play = printPlay()

        computerPlay = random.choice(validPlays)
        
        winner = checkWinner(computerPlay, play)

        print(f"\nPlayer: {play}\nComputer: {computerPlay}")
        print("Draw") if winner == "Draw" else print(f"{winner} won!")
        print("Do you want to play again? (yes/no): ")

        continuePlay = input().lower()


if __name__ == '__main__' :
    main()