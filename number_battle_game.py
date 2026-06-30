print("===== NUMBER BATTLE GAME =====")

target = 7

player_score = 0
computer_score = 0

computer_moves = [2, 4, 6, 8, 10]

for round_num in range(5):

    print("\nRound", round_num + 1)

    player = int(input("Enter number (1-10): "))

    # check invalid input
    if player < 1 or player > 10:
        print("❌ Invalid input!")
        continue

    # computer move
    computer = computer_moves[round_num]

    print("Computer chose:", computer)

    # pass rule
    if player == 7:
        pass

    # distance from target
    player_distance = abs(player - target)
    computer_distance = abs(computer - target)

    print("Your distance:", player_distance)
    print("Computer distance:", computer_distance)

    # scoring logic
    if player_distance < computer_distance:
        player_score += 1
        print("🏆 You win this round!")

    elif player_distance > computer_distance:
        computer_score += 1
        print("💻 Computer wins this round!")

    else:
        print("🤝 Round draw!")

# final result
print("\n===== FINAL RESULT =====")
print("Your Score:", player_score)
print("Computer Score:", computer_score)

if player_score > computer_score:
    print("🎉 YOU WIN THE GAME!")
elif player_score < computer_score:
    print("💀 COMPUTER WINS!")
else:
    print("🤝 MATCH DRAW!")
    