import random

def pyc():
    player_score = 0
    computer_score = 0
    player = ""

    print("""Welcome to Rock Paper Scissors game!
    You can choose Rock[R], Paper[P], Scissors[S] or type 'exit' if you're done
    Let's start!!!""")

    while True:
        player = input(f"Please select [R]Rock, [P]Paper, [S]Scissors\n")
        computer = random.choice(["R", "P", "S"])
        if (player.upper() != "R") & (player.upper() != "P") & (player.upper() != "S") & (player.lower() != "exit"):
            print("Please select only given characters.")
        else:
            if ((player.upper() == "R") & (computer == "S")) | ((player.upper() == "S") & (computer == "P")) | ((player.upper() == "P") & (computer == "R")):
                print(f"player: {player}, computer: {computer}")
                print("You Win")
                player_score += 1
            elif (player.upper() == computer):
                print(f"player: {player}, computer: {computer}")
                print("Tie")
            elif player == "exit":
                break
            else:
                print(f"player: {player}, computer: {computer}")
                print("You Lose")
                computer_score += 1

    print(f"Summary:\nplayer score = {player_score}\ncomputer score = {computer_score}")
    
pyc()
