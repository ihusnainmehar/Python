secret_number = 9
Guess_Count = 0
guess_limit = 3
while Guess_Count<guess_limit:
    Guess = int(input('Guess: '))
    Guess_Count +=1
    if Guess == secret_number:
        print("You Won!")
        break
else:
    print('Sorry! You Failed')