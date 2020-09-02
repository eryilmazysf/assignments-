print ("""***********************
user entrance site
***********************""")
name1="yusuf"
parola1=123456
name=str(input("enter your user name:"))
password=int(input("enter your password:"))
if(name!=name1 and parola1==password):
    print("you did enter your name wrongly")
elif(name==name1 and parola1!=password):
    print("you did enter your password wrongly")
elif(name!=name1 and parola1!=password):
    print("your password and name is wrong")
else:
    print("welcome our websites")
