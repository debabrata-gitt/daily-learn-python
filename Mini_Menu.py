while True:
    print("\n1. Say Hello")
    print("2. Say Bye")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Hello!")

    elif choice == "2":
        print("Goodbye!")

    elif choice == "3":
        print("Program ended")
        break

    else:
        print("Invalid choice")