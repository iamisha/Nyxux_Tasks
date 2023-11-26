try:
    
    user_number = int(input("Enter a number: "))

    
    squares = [x**2 for x in range(1, user_number + 1)]

    
    print("List of squares:", squares)

except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
