print("""
*************************
    WELCOME THE YUSUF BANK
    
Please choose your transaction:

1-)Balance

2-)Cash Deposit

3-)Withdrawal 

for quit enter q   
*************************
""")
balance=1000
while True:
    choose=input("which transaction do you want do:")
    if(choose=="q"):
        print("hope to see you again...")
        break
    elif (choose=="1"):
        print("your balance {} $:".format(balance))
    elif (choose=="2"):
        amount=int(input("please enter cash deposit amount:"))
        balance+=amount
    elif(choose=="3"):
        withdrawal=int(input("please enter amount how much money do you want "))
        if(balance-withdrawal<0):
            print("you can not withdrawal")
        else:
            balance-=withdrawal
