def line():
    print("="*50)

line()
print("\t ELITE HUNTER: PYTHON EDITION ") 
line()

print("\n Welcome to the ELITE HUNTER : PYTHON EDITION game! ")
line()

character_name = input("\n Please enter your character name:- ").upper()
character_age=int(input("\n Please enter your character age:- "))
score = 0
lives = 3


def profile():
    line()
    print(f"PROFILE: {character_name}")
    line()

    print(f"""\n
   
        1. character_name: {character_name}
        2. character_age: {character_age}
        3. score :- {score}      
        4. lives :- {lives}
        """)
          
line()

def story():
    line()
    print("-:OFFICIAL STORY LINE:-")
    line()

    story=f"""\n
    📅 YEAR: 2050

    A mysterious cyber-criminal organization known as **Black Raven**
    has infiltrated government networks and stolen highly classified
    intelligence from the National Intelligence Agency (NIA).

    The organization is demanding billions of dollars in exchange for
    the stolen data. If their demands are not met, they will launch a
    massive cyberattack and permanently shut down the NIA's central
    servers, putting the country's national security at risk.

    You are **Agent {character_name}**, the newest elite operative of
    the National Intelligence Agency (NIA).good luck agent {character_name} !"""

    print(story.upper())
def missions():
    line()
    def mission_1():
        global score, lives
        line()
        print("\t OPERATION :- SILENT ENTRY  ")
        line() 
        mission_1_story=f"\nEnter the enemy headquarters without raising suspicion."
        print(mission_1_story.upper())
        while lives>0 : 
            print("""
            1. Enter through the front door
            2. Use the ventilation system
            3. Climb the roof
            """)
            
                
            choice = input("Enter your choice:- ")
        
            if choice == "1":
                    print("\nYou were spotted by the guards and captured. Mission failed.")
                    lives-=1
                    print("\n press enter to continue...")
                    input()
                    continue
            elif choice == "2":
                        print("\nYou successfully navigated the ventilation system and entered the headquarters undetected. Mission accomplished!")
                        score+=10
                        print(f"\n WELL DONE AGENT {character_name} ! YOUR CURRENT SCORE IS {score}")
                        break
            elif choice == "3":
                        print("\nYou climbed the roof but slipped and fell, injuring yourself. Mission failed.")
                        lives-=1
                        print("\n press enter to continue...")
                        input()
                        continue 

            else:
                        print("\nInvalid choice.")
                        print("\n press enter to continue...")
                        input()
                        continue

        
    def mission_2():
        global score, lives
        line()
        print("\t OPERATION :- HACK THE SECURITY SYSTEM  ")
        line() 
        line_1()
        print("\n< MISSION :- PART - 1 >")
        mission_2_story=f"\nYour mission is to hack or break into the enemy's security system and extract the data and sensitive information."
        print(mission_2_story.upper())

        while lives>0 : 
            secret_code= 2468
            print("Hint:")
            print("- 4 digits")
            print("- Starts with 2")
            print("- Ends with 8")
            print("- Even numbers only")
            print("<you have 3 attempts to guess the correct security PIN>")

            for attempt in range (1,4) :
                print('\n ATTEMPT', attempt , "0ut of 3")

                guess=int(input("enter security PIN :-")) 

                if guess<1000 or guess >9999 :
                    print("INVALID number")
                    lives-=1
                    print("\n press enter to continue...")
                    input()
                    continue

                elif guess == secret_code :
                    print("CORRECT PASSWORD ! ")
                    lives+=1
                    score+=10
                    print(f"\n WELL DONE AGENT {character_name} ! YOUR CURRENT SCORE IS {score}. now, extract the data and sensitive information.")
                    print("\n press enter to continue...")
                    input()
                    break
                else :
                    print("INCORRECT PASSWORD !")
                    lives-=1
                    print("\n press enter to continue...")
                    input()
            else:
                print("\nCOMPUTER LOCKED.")
                print("\n MISSION FAILED! BETTER LUCK NEXT TIME.")
                print("\n press enter to continue...")
                input()
                break

             
            line()
            print("\t OPERATION :- EXTRACT DATA  ")
            print("\t <PART - 2> ")
            line()
            line_1()
            print("\n< COMPUTER SERVER >")    
            line_1()
            mission_2_2_story=f"\nYour mission is to infiltrate the enemy's computer server and extract the data and sensitive information."
            print(mission_2_2_story.upper())
            print("\nSearching for 'file' in the enemy's computer server...")
            print("""   
                        -NIA classified files
                        -BLACK RAVEN financial records
                        -NIA personnel records
                        -BLACK RAVEN communication logs
                                """)
            search_term = input("\nEnter the file name to find the data: ")

                
            if search_term.lower() == "NIA classified files".lower():
                    print("\nData found! Extracting the data and sensitive information...")
                    score+=10
                    lives+=1
                    print(f"\n WELL DONE AGENT {character_name} ! YOUR CURRENT SCORE IS {score}. now, exit the enemy headquarters without raising suspicion.")
                    print("\n press enter to continue...")
                    input()
            elif search_term.lower() == "BLACK RAVEN financial records".lower():
                    print("\nData not found! Mission failed.")
                    score-=10
                    print("\n press enter to continue...")
                    input()
            elif search_term.lower() == "NIA personnel records".lower():
                    print("\nData not found! Mission failed.")
                    score-=10
                    print("\n press enter to continue...")
                    input()
            elif search_term.lower() == "BLACK RAVEN communication logs".lower():
                    print("\nData not found! Mission failed.")
                    score-=10
                    print("\n press enter to continue...")
                    input()    
            else:
                    print("\nInvalid search term! Mission failed.")
                    score-=10
                    print("\n press enter to continue...")
                    input()

            print("\n <MISSION COMPLETE> ")
            break

    def mission_3():
        global score, lives
        line()
        print("\t OPERATION :- ESCAPE THE HEADQUARTERS  ")
        line() 
        mission_3_story=f"\nYour mission is to escape the enemy headquarters without raising suspicion."
        print(mission_3_story.upper())
        while lives>0 : 
            print("""
            1. Exit through the front door
            2. Use the ventilation system
            3. Climb the roof
            """)
            choice = input("Enter your choice:- ")
            if choice == "1":
                print("\nYou were spotted by the guards and captured. Mission failed.")
                lives-=1
                print("\n press enter to continue...")
                input()
                continue
            elif choice == "2":
                print("\nYou successfully navigated the ventilation system and exited the headquarters undetected. Mission accomplished!")
                score+=10
                print(f"\n WELL DONE AGENT {character_name} ! YOUR CURRENT SCORE IS {score}")
                break
            elif choice == "3":
                print("\nYou climbed the roof but slipped and fell, injuring yourself. Mission failed.")
                lives-=1
                print("\n press enter to continue...")
                input()
                continue    
            else:
                print("\nInvalid choice.")
                print("\n press enter to continue...")
                input()
                continue

        print("\n <MISSION COMPLETE> ")

        print("\nCongratulations! You have completed all the missions and successfully extracted the data and sensitive information from the enemy headquarters.")
        print(f"\nThank you for playing the game, Agent {character_name}!")
        line()
        print("GOODBYE !")
        line()

    mission_1()
    mission_2()
    mission_3()
def rules():
    line()
    print("\t RULES OF THE GAME ")
    line()
    print("""
    1. You have 3 lives in total.
    2. Each mission has a specific objective that must be completed to progress.
    3. If you fail a mission, you will lose a life and have to restart the mission.
    4. If you lose all your lives, the game is over.
    5. You can view your profile and score at any time from the home.
    6. Make sure to read the story and follow the instructions carefully to succeed in your missions.
    """)

def line_1():
    print("="*12)
while True:
    line_1()
    print(" HOME ")
    line_1()

    print("""  
       1. start missions
       2. view profile
       3. story
       4. rules   
       5. exit
    """) 

    choice_1 = input("Enter your choice (1-5): ")

    if choice_1 == "1":
        missions()
    elif choice_1 == "2":
        profile()
        input("\nPress Enter to continue...")
    elif choice_1 == "3":
        story()
        input("\nPress Enter to continue...")
    elif choice_1 == "4":
        rules()
        input("\nPress Enter to continue...")
    elif choice_1 == "5":
        print("Thank you for playing the game!")
        break
    else:
        print("Invalid choice! Please try again")