a = input("Enter a word: ")
print(a)
for character in a :
    
    if character == "A" or character == "a":
        print("You have found the letter A")
        break
    else:
        print("A not found")
