winning_number=20

print("This a number guessing game")
input_number=int(input("Guess your number between 1to 100:"))

guess=1
game_over =False

while not game_over:
    if(winning_number==input_number):
        print(f"You win!,and guess the number in {guess} time")
        game_over=True
    else:
        if(winning_number>input_number):
            print("You guess too low!")
            guess+=1
            input_number=int(input("guess again:"))
        else:
            print("You guess to high!")
            guess+=1
            input_number=int(input("guess again:"))

