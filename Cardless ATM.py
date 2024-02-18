while True:
    account_no=6569
    password=1234
    acc_balance=100
    main_options=int(input('''select
                            1.UPI Cardless Cash
                            2.Enter Account number'''))
    if main_options==1:
        scanner=int(input("scanner here"))
        if scanner==account_no:
            second_options=int(input('''select the service:
                                    1.Cash Withdrawal
                                    2.Cash Deposit 
                                    3.Check Your Account Balance
                                    4.Get mini statement'''))
            if second_options==1:
                withdraw=int(input("Enter The Amount"))
                print("Collect The Money")
                Amount=acc_balance-withdraw
                print("Your Remaining Balance is;",Amount)
            elif second_options==2:
                Deposit=int(input("Enter The Deposit Amount"))
                print("transaction completed")
                adding=acc_balance+Deposit
                print('Now Your Account Balance is;', adding)
            elif second_options==3:
                print("Your Account Balance is;",acc_balance)
            elif second_options==4:
                print('''Your Recent transactions;
                    Withdrawal=200
                    Transfer=100
                    Bank chargers 25
                    Now Your Account Balance''',acc_balance)
            else:
                print("Please Choose Correct Option")
        else:
            print("Please Scan Again")
    elif main_options==2:
        match=int(input("Enter Your Account number"))
        pwd=int(input("Enter Your PIN"))
        if match==account_no and pwd==password:
            third_options=int(input('''select the service:
                                    1.Cash Withdrawal
                                    2.Cash Deposit 
                                    3.Check Your Account Balance
                                    4.Get mini statement
                                    5.Change the PIN'''))
            if third_options==1:
                withdraw=int(input("Enter The Amount"))
                print("Collect The Money")
                Amount=acc_balance-withdraw
                print("Your Remaining Balance is;",Amount)
            elif third_options==2:
                Deposit=int(input("Enter The Deposit Amount"))
                print("transaction completed")
                adding=acc_balance+Deposit
                print('Now Your Account Balance is;', adding)
            elif third_options==3:
                print("Your Account Balance is;",acc_balance)
            elif third_options==4:
                print('''Your Recent transactions;
                    Withdrawal=200
                    Transfer=100
                    Bank chargers 25
                    Now Your Account Balance''',acc_balance)
            elif third_options==5:
                new_pwd=int(input("Enter New Password"))
                again=int(input("Again Enter New Password"))
                if new_pwd==again:
                    password=new_pwd
                    print("Updated password:",password)
                else:
                    print("Passwords do not match. Please try again.")
            else:
                print("Please choose Correct Option")
        else:
            print("Passwords or Account number is Worng. Please try again.")
            break
    else:
                print("Please Choose Correct Option")