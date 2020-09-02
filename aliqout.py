def aliqout(number):
    mylist=list()
    for i in range(2,number+1):
        if(number%i==0):
            mylist.append(i)
    print(mylist)
while True:
    number=input("enter a number:")
    if(number=="q"):
        print("exiting....")
        break
    else:
        number=int(number)
        aliqout(number)
