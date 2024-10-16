secret_number = 6
guess_limit = 5
guess_count = 0
while guess_count<guess_limit:
    guess = int(input("Enter Your Guess: "))
    guess_count +=1
    if guess == secret_number:
        print("You Won!")
        break
    elif guess>secret_number:
        print("Too High")
    elif guess<secret_number:
        print("Too Low")
else:
    print("Sorry! You Failed")