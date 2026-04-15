correct_pin = 1234 
attempts = 3 
while attempts > 0: 
pin = int(input("Enter your PIN: ")) 
 
    if pin == correct_pin: 
        print("Access Granted") 
        break 
    else: 
        attempts -= 1 
        print("Incorrect PIN. Attempts left:", attempts) 
 
if attempts == 0: 
    print("Too many incorrect attempts. Card blocked.") 
    exit() 
 
 
def check_balance(balance): 
    print("Your balance is:", balance) 
 
def deposit_money(balance): 
    deposit = int(input("Enter deposit amount: ")) 
    balance += deposit 
    history.append("Deposited: Rs. " + str(deposit)) 
    print(deposit, "deposited successfully") 
    return balance 
 
def withdraw_money(balance): 
    withdraw = int(input("Enter withdrawal amount: ")) 
    if withdraw <= balance: 
        balance -= withdraw 
        history.append("Withdrew: Rs. " + str(withdraw)) 
        print("Rs.", withdraw, "withdraw successful") 
    else: 
        print("Insufficient balance!") 
    return balance 
 
balance = 15000 
history = [] 
 
while True: 
    print("\nSmartBank ATM") 
    print("1. Check balance") 
    print("2. Deposit") 
    print("3. Withdraw") 
    print("4. Transaction history") 
    print("5. Exit") 
 
    choice = int(input("Enter choice: ")) 
 
    if choice == 1: 
         print("Your balance is:", balance) 
 
    elif choice == 2: 
        balance = deposit_money(balance) 
 
    elif choice == 3: 
        balance = withdraw_money(balance) 
 
    elif choice == 4: 
        print("\nTransaction history")     
        if len(history) == 0: 
            print("No transactions yet") 
        else: 
            for transaction in history: 
                print(transaction) 
 
    elif choice == 5: 
        print("Visit again!") 
        break 
 
    else: 
        print("Invalid choice")
