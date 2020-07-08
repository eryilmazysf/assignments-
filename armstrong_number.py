number=input("enter a number:")
a=list(number)

if '.' in a:
    while not number.isdigit():
        number=input('please enter a integer number:')
elif ','in a:
    while not number.isdigit():
        number=input('please enter a integer number:')
elif number.isalpha():
    print('Do not use any entries other than numeric values please enter a digit number:')
    while not number.isdigit():
        number=input("enter a digit number:")
elif int(number)<0:
    print('you should enter positive number')
    while not number.isdigit():
        number =(input("enter a integer number:"))

x=len(str(number))
number1=int(number)
number2=int(number)
sum=0
digit_number=0
while(number1>0):
    digit_number=number1%10
    sum+=digit_number**x
    number1//=10
if (sum==number2):
    print("{} is a amstrong number".format(number))
else:
    print("{} is not a amstrong number".format(number))
