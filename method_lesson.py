def meeting():
    print("hello welcome..")
meeting()
def addition(a,b,c):
    print("addition of value:",a+b+c)
addition(5,6,7)
def factorial(number):
    x=1
    if(number==0 or number==1):
        print("factorial:",x)
    else:
        while(number >=1 ):
            x*=number
            number-=1
        print(x)
y=int(input("what factorial number do you want to calculate :"))
factorial(y)