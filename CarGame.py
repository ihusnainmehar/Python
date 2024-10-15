command = ""
started = False
while True:
    command = input("> ").lower()
    if command =="help":
        print("""
start - to start the Car
stop - to stop the Car
quit - to exit
""")
    elif command =="start":
        if started:
            print("Car is Already started!!!!!!!!!")
        else:
            started = True
            print('Car Started!, Ready to go!!!!!')
    elif command == "stop":
        if not started:
            print("Car is already stopped!!!!!!")
        else:
            started = False
            print("Car Stopped")
    elif command == "quit":
        break
    else:
        print("I don't understand that")