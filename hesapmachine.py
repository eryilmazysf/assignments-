print("""" ******************************
C   A   L   C   U   L   A   T   A   R
Chose your process name :
1.addition
2.subtraction
3.multiplication
4.division
5.exponentiate


********************************
""")
x=int(input("enter first number:"))
y=int(input("enter second number:"))
a=int(input("enter your process:"))
if a==1:
    print("{} with {} result of addition :{}".format(x,y,x+y))
elif a==2:
    print("{} with {} result of subtraction :{}".format(x,y,x-y))
elif a==3:
    print("{} with {} result of multiplication :{}".format(x,y,x*y))
elif a==4:
    print("{} with {} result of division :{}".format(x,y,x/y))
elif a==5:
    print("{} with {} result of exponentiate :{}".format(x,y,x**y))

else:
    print("invalid process please try again")
