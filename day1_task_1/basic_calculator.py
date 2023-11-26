print("Basic Calculator using Python")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
res = 0

print("Choose 1 to 4 options avilable:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input())

if choice == 1:
    res = num1 + num2
elif choice == 2:
    res = num1 - num2
elif choice == 3:
    res = num1 * num2
elif choice == 4:
    if num2 != 0:  # Check for division by zero
        res = num1 / num2
    else:
        print("Error: Division by zero is not allowed")
        exit()  # Terminate the program if division by zero is attempted
else:
    print("Please choose a valid option")

print("Your result:", res)
