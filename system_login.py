print("""
******************************
USER LOGİN PAGE
******************************
""")
registered_name="yusuf"
registered_password="123456"
enter_limit=3
while True:
    name = input("enter your name:")
    password =input("enter your password:")
    if(name != registered_name and password==registered_password):
        print("name is wrong")
        enter_limit-=1
    elif(name == registered_name and password!=registered_password ):
        print("password is wrong")
        enter_limit -= 1
    elif (name != registered_name and password!=registered_password ):
        print("name and password is wrong")
        enter_limit -= 1
    else:
        print("welcome the page...")
        break
    if (enter_limit==0):
        print("your limit right is finish")
        break
