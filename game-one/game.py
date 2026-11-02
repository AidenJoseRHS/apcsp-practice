import random


manual = input("move: ")

# Define your own functions here.

def random_move():
    return random.randint(0, 2)

def judgement():
    if move1 == 0 and move2 == 1:
        print("a")
    else:
        print("b")
        
ai = random_move()

    # Build your playable game here, calling your functions.
def main():
player1move = manual
player2move = ai
move1 = player1move
move2 = player2move
player1 = 0
player2 = 0
while player1Move != player2move:
    player1Move = manual
    player2move = ai
return move2


if __name__ == "__main__":
    main()