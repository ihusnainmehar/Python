import sys
Account_Holder = 'User'
Account_Number= 784512
PIN = 4321
Balance= 2500.00
Account_Type= "Savings"

#Welcome Screen
print('''=============================
******** Welcome to Python Bank ********
=============================''')
Account_Number_v = int(input("Enter Account Number: "))
PIN_v = int(input("Enter PIN: "))
if Account_Number == Account_Number_v and PIN == PIN_v:
    print(f'''=============================
    Dashboard
    =============================
    
    Welcom User!
    
    Account Type = {Account_Type}
    Current Balance = {Balance:.2f}
Choose Transaction:

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Account Information
6. Exit''')
    transaction = int(input("Choose Transaction: "))
else:
    print('''Access Denied!
    Invalid Account No or PIN''')
    sys.exit()

if transaction == 1:
    print("Available Balance: €", Balance)
elif transaction == 2:
    D_Amount = int(input("Enter Deposit Amount: €"))
    if D_Amount <=0:
        print("Invalid Amount: ")
    else:
        New_Balance = Balance + D_Amount
        print("Deposit Successful!")
        print("Previous Balance: €", Balance)
        print("Amount Deposited: €", D_Amount)
        print("New Balance: €", New_Balance)
elif transaction == 3:
    W_Amount = int(input("Enter Witdrawal Amount: €"))
    fee = 0
    is_suspicious = False
    if W_Amount>1000:
        is_suspicious = True
    else:
        is_suspicious = False
    if is_suspicious == True:
        print('''⚠ SECURITY NOTICE

This transaction has been flagged for additional verification.''')
    if W_Amount <=0:
        print("Invalid Amount")
    elif W_Amount > Balance:
        print("Withdrawal Amount Cannot be exceeded than Available amount")
    elif Balance - W_Amount - fee <100:
        print("The bank requires a minimum remaining balance of 100 €")
    else:
        print("Withdrawal Successful")
        if W_Amount>=1000:
            fee = (W_Amount/100)*2
            New_Balance = Balance - W_Amount -fee
        else:
            New_Balance = Balance - W_Amount
        print("Previous Balance: €", Balance)
        print("Amount Withdrawn: €", W_Amount)
        print("Fee: ", fee)
        print("New Balance: €", New_Balance)
elif transaction == 4:
    print('''========== Transfer Money ==========''')
    T_fee = 0
    R_Account = input("Receiver Account Number: ")
    R_Account.isdigit()
    T_Amount = int(input("Transfer Amount: "))
    is_suspicious = False
    if T_Amount>1500:
        is_suspicious = True
    else:
        is_suspicious = False
    if is_suspicious == True:
        print('''⚠ SECURITY NOTICE

This transaction has been flagged for additional verification.''')
    if T_Amount<=500:
        T_fee = 2
    elif T_Amount>500 and T_Amount<=1000:
        T_fee = 5
    elif T_Amount>1000 and T_Amount<=2000:
        T_fee = (T_Amount/100)
    else:
        T_fee = (T_Amount/100)*1.5

    Deduction = T_Amount + T_fee
    if len(R_Account)!=6 or not R_Account.isdigit():
        print("Invalid Reciever Account")
    elif R_Account == Account_Number:
        print("You cannot transfer money to your own account!")
    elif T_Amount <= 0:
        print("Invalid Amount")
    elif Deduction > Balance:
        print("Insufficeint Balance!")
    elif Balance - T_Amount - T_fee<100:
        print("You Have to maintain at least 100 euros in your account")
    else:
        New_Balance = Balance - T_Amount - T_fee
        print("Previous Balance: €", Balance)
        print("Amount Transfered: €", T_Amount)
        print("Fee: ", T_fee)
        print("Total Deductio: ", Deduction)
        print("New Balance: €", New_Balance)
elif transaction == 5:
    account = str(Account_Number)
    masked = "*" * (len(account) - 4) + account[-4:]
    print(f'''========================================
          ACCOUNT INFORMATION
========================================

Account Holder: {Account_Holder}
Account Number: {account}
Account Type: {Account_Type}
Available Balance: {Balance:.2f}
Account Status: Active''')
elif transaction == 6:
    print('''Thank you for using Python Digital Bank.

Session ended successfully.''')
    sys.exit()
else:
    print("Invalid Selection")
    sys.exit()