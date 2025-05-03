# mathappupdatedlambda.py

# Defining basic mathematical operations using lambda functions
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Cannot divide by zero"

# Function to display the menu to the user
def show_menu():
    print("\nWelcome to the Math App!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main function to drive the app
def math_app():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The result of {num1} + {num2} is: {add(num1, num2)}")

        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")

        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")

        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")

        elif choice == '5':
            print("Exiting the Math App. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the app
if __name__ == "__main__":
    math_app()
