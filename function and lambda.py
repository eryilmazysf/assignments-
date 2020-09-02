def asalmı(a):
    if(a==2):
        print("asaldır")
    elif (a%2==0 ):
        print("asal değil:")
    else:
        print("asaldır")
asalmı(79)
a=6         #global
def function():
    global a #local olan a değerini global yaptık
    a=5
    print(a)
    return a

function()
print(a)
def minus(a,b):
    return a-b
minus1=lambda m,n:m-n
print(minus(10,6))
print(minus1(20,10))









