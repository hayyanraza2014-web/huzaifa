print("=================================================")
print("\t SIMPLE NUMBER GUESSING")
print("=================================================")

secret_number= 34

for attempt in range (1,11) :
    print('\n ATTEMPT', attempt , "0ut of 10")

    guess=int(input("enter your guess (1-100) :-")) 

    if guess<1 or guess >100 :
        print("INVALID number")
        continue

    if guess == secret_number :
        print("🎉 Congratulations! your guess number is correct")
        break
    elif guess > secret_number :
        print("yoy are too high !")

    elif guess < secret_number :
        print("you are too low") 
else :
    print("\n💀 Game Over! Better luck next time.")
         