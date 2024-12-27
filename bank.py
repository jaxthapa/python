#Initial setup
balance = 1000
print("Welcome To My ATM")

while True:
    #Menu Display
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice =input("Choose an option (1-4)?:")
    if choice =="1":
        print(f"Your Current Balance is :${balance}")
    elif choice =="2":
        amount= float(input("Enter Your Amount : $"))
        balance += amount
        print(f"Deposit Sucessful ! New balance :${balance}")
    elif choice =="3":
        amount =float(input("Withdraw Amount:$"))
        if amount <= balance:
            balance -= amount
            print(f"Current Balance :${balance}")
        else:
            print("insufficient balance")
    elif choice == "4":
        print("thank you")
        break
    else:
        print("invalid code")
        
        
   
