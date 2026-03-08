import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def calculator():

    while True:
        clear_screen()

        print("=" * 40)
        print("        SIMPLE CALCULATOR")
        print("=" * 40)

        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        print("-" * 40)

        choice = input("Select an option (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid option. Please try again.")
            input("Press Enter to continue...")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number input.")
            input("Press Enter to continue...")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        print("\nResult:", result)

        input("\nPress Enter to continue...")


calculator()