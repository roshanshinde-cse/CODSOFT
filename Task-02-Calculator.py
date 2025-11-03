# Task-02-Calculator/calculator.py

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Error: Division by zero"

while True:
    print("\n=== Simple Calculator ===")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Exiting calculator...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {sub(num1, num2)}")
    elif choice == '3':
        print(f"Result: {mul(num1, num2)}")
    elif choice == '4':
        print(f"Result: {div(num1, num2)}")
    else:
        print("Invalid input!")
