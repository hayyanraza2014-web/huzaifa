def line():
    print("=" * 40)

line()
print("\t🧠 BRAIN BATTLE")
line()

score= 0
lives= 3

riddle=[
    {"question":"Which came first, the chicken or the egg?","answer":"chicken"},
    {"question":"If somebody tell a lie and say; I am lying, is he telling the truth or lying?", "answer":"truth"},
    {"question":"What belongs to you but is used more by other people?", "answer":"name" }
 ]
math_questions = {
    "easy": [
        {"question": "What is 15 + 27?", "answer": "42"},
        {"question": "What is 12 * 8?", "answer": "96"},
        {"question": "What is 100 / 4?", "answer": "25"}
    ],

    "medium": [
        {"question": "What is 25% of 80?", "answer": "20"},
        {"question": "What is the square root of 144?", "answer": "12"},
        {"question": "What is 7^3?", "answer": "343"}
    ],

    "hard": [
        {"question": "What is 17 * 19?", "answer": "323"},
        {"question": "Solve: 3x + 9 = 24. What is x?", "answer": "5"},
        {"question": "What is the cube root of 125?", "answer": "5"}
    ],

    "boss": [
        {"question": "A farmer has 17 sheep. All but 9 die. How many are left?", "answer": "9"},
        {"question": "What is half of 2 plus 2?", "answer": "3"},
        {"question": "I am an odd number. Remove one letter and I become even. What number am I?", "answer": "seven"}
    ]
}
def play_math_quiz():
    levels = ["easy", "medium", "hard", "boss"]

    for level in levels:

        print(f"\n===== {level.upper()} LEVEL =====")

        score = 0

        for q in math_questions[level]:

           print("\n" + q["question"])

           user_answer = input("Answer: ")

           if user_answer.lower() == q["answer"].lower():
              print("✅ Correct")
              score += 1
           else:
                print("❌ Wrong")
                print("Correct Answer:", q["answer"])

        if score < 2:
         print("🚫 Level Failed!")
         break
    else:   
        print("🎉 Level Passed!")
def play_quiz(questions):
    global score, lives

    for q in questions:
        if lives == 0:
            print("\n💀 Game Over!")
            return

        print("\n" + q["question"])
        user_answer = input("Your Answer: ")

        if user_answer.lower() == q["answer"].lower():
            print("✅ Correct!")
            score += 1
            lives += 1
            print("❤️ Lives :", lives)
        else:
            print("❌ Wrong!")
            print("Correct Answer:", q["answer"])
            lives -= 1
            print("❤️ Lives Left:", lives)    

while True:
    

    print("1. Start riddle Quiz")
    print("2. Start math Quiz")
    print("3. Rules")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        play_quiz(riddle)

    elif choice == "2":
        play_math_quiz()

    elif choice == "3":
        print("\nRULES")
        print("- You have 3 lives.")
        print("- Correct answer = 1 point.")
        print("- Wrong answer loses 1 life.")
        print("- Game ends when lives reach 0.")

    elif choice == "4":
        break

    else:
        print("Invalid Choice!")

line()
print("\tRESULT")
line()

print("Score:", score)

if score >= 5:
    print("🏆 Quiz Master")
elif score >= 3:
    print("🥈 Quiz Warrior")
else:
    print("📚 Beginner")

print("Thanks for playing!")
































































































































































