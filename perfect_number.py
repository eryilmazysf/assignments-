x=int(input("please enter a number:"))
i=1
sum=0
while(i<x):
    if(x%i==0):
        sum+=i
    i+=1
if(sum==x):
    print("this number is perfect number")
else:
    print("this number is not perfect")


