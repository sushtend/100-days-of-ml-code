started=False
cmd=""

while cmd.lower() != 'quit':
    cmd=input("> ")

    if cmd.lower()=="help":
        
            print("start - to start the car")
            print("stop - to stop the car")
            print("quit - to exit")
    elif cmd.lower()=="start":
        if started:
            print("already started")
        else:
            started=True
            print("car started")
    elif cmd.lower()=="stop":
        if not started:
            print("already stopped")
        else:
            started=False
        print("stopped")
    elif cmd.lower()=="quit":
        break
    else:
        print("sorry, i can't understand that")
