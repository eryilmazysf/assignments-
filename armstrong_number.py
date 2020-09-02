number=input("enter a number:")
x=len(number)
number1=int(number)
number2=int(number)
sum=0
digit_number=0
while(number1>0):
    digit_number=number1%10
    sum+=digit_number**x
    number1//=10
if (sum==number2):
    print("amstrong number")
else:
    print("not amstrong")
