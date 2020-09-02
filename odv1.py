weight=int(input("enter your weight:"))
length=float(input("enter your length as metre:"))
index=weight/(length*length)
if(index<=18.5):
    print("you are thin")
elif(index>18.5 and index<25):
    print("you are normal")
elif(index>=25 and index<30):
    print("you are fat")
else:
    print("you are obese")
