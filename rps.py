import random



def main(x1,y1):
    player1 = x1
    computer1 = y1

    def computers_move():
        computer_choices = ['rock', 'paper','sissors']
        computer_rand = random.randint(0,2)
        return computer_choices[computer_rand]

    def players_move():
        players_choice = input("Choose a move\n1: Rock\n2: Paper\n3: Sissors\nCHOICE: ")
        if players_choice == '1':
            return 'rock'
        elif players_choice == '2':
            return 'paper'
        elif players_choice == '3':
            return 'sissors'
        else:
            return 'incorrect choice'
            
    def game(pm, cm):
        x =pm
        y=cm
        print(f"PLAYERS MOVE: {x}")
        print(f"COMPUTERS MOVE: {y}")

        cs = 0
        ps = 0
        if x == y:
            print("TIE!!")
        elif x == "rock" and y == "sissors":
            print("WINNER: PLAYER1")
            ps +=1
        elif x == "sissors" and y == "paper":
            print("WINNER: PLAYER1")
            ps +=1
        elif x == "paper" and y == "rock":
            print("WINNER: PLAYER1")
            ps +=1
        else:
            print("WINNER: COMPUTER")
            cs += 1
        print("\n\n")
        return ps,cs

    computerChoice = computers_move()
    playersMove = players_move()

    if playersMove == 'incorrect choice':
        print("Selected the wrong choice, please play again")
        
        
    playGame = game(playersMove, computerChoice)
    
    player1 = player1 + playGame[0]
    computer1 += playGame[1]

    return player1, computer1

def game():
    print("Welcome to ROCK, PAPER, SISSORS.\nThis is a Best of 5, highest score wins")
    i=0
    x1 = 0
    y1 = 0
    for i in range(5):
        print(f"GAME {i+1}")    
        x = main(x1, y1)
        x1 = x[0]
        y1 = x[1]
        i+=1

    print(f"THE FINAL SCORE IS:\nPLAYER1: {x1}\nCOMPUTER: {y1}")        
    if x1 > y1:
        print("PLAYER 1 WINS")
    elif x1 < y1:
        print("COMPUTER WINS")
    else:
        print("GAME IS A DRAW")
game()