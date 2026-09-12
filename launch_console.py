name = input("What's your name? ")
print("Welcome to " + name + "'s Launch Console!")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Fun Fact")
    print("4) Exit")
    choice = input("Pick 1-4: ")
    if choice == "1":
        print("I am trying to learn lua.")
    elif choice == "2":
        print("My current goal is to develop a game.")
    elif choice == "3":
        print("I love animals")
    elif choice == "4":
        print("Goodbye")
        running = False
    else:
        print("Please pick 1, 2, 3, or 4.")