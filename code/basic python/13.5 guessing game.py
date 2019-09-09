Guess_count=1
guess=9

print("+++++ This program lets you guess the secret number +++++")
while Guess_count<=3:
    num = int(input("Gues the number: "))
    if guess==num:
        print("Correct")
        #exit()
        break
    Guess_count+=1
# Else for while loop evaluates after completion of all loops without brteak
else : 
    print("Sorry you failed")