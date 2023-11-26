number = int(input("Enter a number: "))
fact = 1

if number < 0:
    print("Please enter a positive number!")
else:
    for i in range(1, number + 1):
        fact *= i
    print("Factorial:", fact)
