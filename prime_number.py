def prime(number):
    for i in range(2,number):
        if(number%i==0):
            return False
    return True

while True:
    number=input("number:")
    if(number=="q"):
        print("quit.....")
        break
    number=int(number)
    if(number==1):
        print("this number is not prime number")
    elif(number==2):
        print("this number is prime number")
    else:
        if(prime(number)):
            print(number,"this number is prime number")
        else:
            print(number,"this number is not prime number")



