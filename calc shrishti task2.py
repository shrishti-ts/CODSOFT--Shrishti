#SHRISHTI SINGH
#CODSOFT Task 2 CALCULATOR beginmer level

# Function to perform arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

# Main program loop
while True:
    print("Options:")
    print("1. Addition: ")
    print("2. Subtraction: ")
    print("3. Multiplication: ")
    print("4. Division: ")
    print("5. Quit: ")
    
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Bye,work finished!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {result}")
    else:
        print("Invalid choice. Please try again.")