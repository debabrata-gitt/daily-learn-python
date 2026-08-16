balance = 5000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = input("Enter your choice: ")

if choice == "1":
    print("Balance =", balance)

elif choice == "2":
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print("New balance =", balance)

elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance -= amount
        print("New balance =", balance)
    else:
        print("Insufficient balance")

else:
    print("Invalid choice")