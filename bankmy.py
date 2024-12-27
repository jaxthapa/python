# Conditional statements

print("Welcome to the jacky ATM")
balance = 2000

print("Choose the option From below")
print("1. Check Balance\n3. Withdraw\nExit")
choice = int(input("Choose number from 1 to 4: "))

if choice==1:
    print(f"Your Current Balance : {balance:.2f}")
elif choice==2:
    amont=float(input("Enter the amount do you want to deposit: ")) 
    balance +=amount
    print(f"{amount:.2f} Balance Deposit Sucessfully\nYour Current Balance : {balance:.2f}")
elif choice==3:
    amount=float(input("Enter the amount do you want to withdraw: "))
    balance -=amount
    
