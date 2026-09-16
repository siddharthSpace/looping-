choice = int(input("Enter your choice: "))

# 1 = Addition
# 2 = Subtraction
# 3 = Multiplication
# 4 = Division
# 5 = Factorial

if choice == 1:

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    output = num1 + num2

elif choice == 2:

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    output = num1 - num2

elif choice == 3:

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    output = num1 * num2

elif choice == 4:

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if num2 == 0:
        print("Cannot divide by zero")
        output = None
    else:
        output = num1 / num2

elif choice == 5:

    num1 = int(input("Enter the number: "))

    output = 1

    for i in range(1, num1 + 1):
        output = output * i

else:

    print("Invalid choice")
    output = None

if output is not None:
    print("Output:", output)