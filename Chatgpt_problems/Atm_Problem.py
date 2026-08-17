balance = 10000
while True:
    print("/n1. balance amount")
    print("n2. Deposit")
    print("n3. money withdrawal")
    print("n4. break")
    
    choice = (input("enter your choice:"))
    
    if choice=="1":
        print("balance amount:" , balance)
    elif choice=="2":
        amount=float(input("enter your amount:"))
        balance += amount
        print("money deposited!")
    elif choice=="3":
        amount=float(input("enter your money:"))
        if amount<= balance:
           balance -= amount
           print("money withdrawn")
        else:
            print("insufficient balance")
    elif choice=="4":
        break
    else:
        print("invalid choice")           
            