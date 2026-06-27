def line():
    print("=" * 40)

def addition(a,b):
    return a + b

def substraction (a,b):
    return a - b 

def multiplication (a,b):
    return a * b

def division (a,b):
     if b == 0:
        return "Error! Cannot divide by zero."
     return a / b 

def floordivision (a,b):
     if b == 0:
        return "Error! Cannot divide by zero."
     return a // b

history = []

while True:
    line()
    print("\tCALCULATOR")
    line()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. floorDivision")
    print("6. View History")
    print("7. Exit")
    line()

    choice = input("Enter your choice (1-7): ")

    if choice == "7":
         print("Thank you for using the calculator!")
         break
    elif choice == "6":
        line()
        print("CALCULATION HISTORY")
        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)
            input("\nPress Enter to continue...")
        continue

    elif choice in ["1", "2", "3", "4","5"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice=="1":
          result= addition(num1 , num2)
          operation="+"

        elif choice=="2":
            result=substraction(num1 , num2)
            operation="-"

        elif choice=="3":   
            result=multiplication(num1 , num2)
            operation="*"

        elif choice =="4":
            result=division(num1,num2)
            operation="/"

        elif choice =="5":
            result=floordivision(num1,num2)
            operation="//"

        print(f"\nResult: {result}")
        history.append(f"{num1} {operation} {num2} = {result}")

        input("\nPress Enter to continue...")

    else:
        print("Invalid choice! Please try again.")







































































