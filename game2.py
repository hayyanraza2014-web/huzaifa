 # project ; tressure hunt game
print("==========================================")
print("\tTRESSURE HUNT GAME")
print("==========================================")
print(" WELCOME TO TRESSURE HUNT")
treasure_box = 5

for attempt in range(1, 8):
    print("\nAttempt", attempt, "out of 7")
    guess=int(input("enter a box number between (1-10) :"))

    if guess<1 or guess>18 :
       print("box number is invalid, try again")
       continue

    if guess== 3 :
     pass

    if guess== treasure_box :
       print("🎉 Congratulations! You found the treasure!")
       break

    elif ( guess < treasure_box):
       print("⬆️ The treasure is in a higher-numbered box.")

    elif guess> treasure_box:
        print("⬇️ The treasure is in a lower-numbered box.")

else:
    print("\n💀 Game Over! Better luck next time.")

