num = int(input("Enter the number of data: "))

# Use list comprehension to get the numbers from user input
l1 = [int(input("Enter any number: ")) for _ in range(num)]

# Calculate sums using built-in functions
sum_even = sum(x for x in l1 if x % 2 == 0)
sum_odd = sum(x for x in l1 if x % 2 != 0)

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
