try:
    
    s1 = set(map(int, input("Enter the first set : ").split()))

    
    s2 = set(map(int, input("Enter the second set: ").split()))
    
    int_res = s1.intersection(s2)
    print("Interesection result: ", int_res)
    
    union_res = s1.union(s2)
    print("Union result: ", union_res)


except ValueError:
    print("Error: Enter the valid number!")
    
except Exception as e:
    print(f"An unexpected error occuring: {e}")


