mess = input("Enter any string: ")
vowels = set("aeiou")
count = 0

for x in mess.lower():
    if x in vowels:
        count += 1

print(count)
