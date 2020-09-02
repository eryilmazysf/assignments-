print("""********************************************
if you find rectangle choose 1 or if you find triangle choose 2:
********************************************""")
x=int(input("what is your decision:"))
if x==1:
    r1 = int(input("enter side1 length:"))
    r2 = int(input("enter side2 length:"))
    r3 = int(input("enter side3 length:"))
    r4 = int(input("enter side4 length:"))
    if (r1==r2==r3==r4):
        print("karedir")
    elif (r1==r2 and r3==r4 ):
        print("dikdörtgen")
    elif (r1==r3 and r2==r4):
        print("dikdörtgen")
    elif (r1==r4 and r2==r3):
        print("dikdörtgen")
    else:
        print("sıradan dikdörtgen")
if x==2:
    t1 = int(input("enter side1 length:"))
    t2 = int(input("enter side2 length:"))
    t3 = int(input("enter side3 length:"))
    if (abs(t1-t2)<=t3<=abs(t1+t2)):
        if(t1==t2 and t2!=t3 ):
            print("ikizkenar üçgen")
        elif(t1==t3 and t2!=t3):
            print("ikizkenar üçgen")
        elif(t1==t2==t3):
            print("eşkenar üçgen")
        else:
            print("sıradan bir üçgen")
    else:
        print("üçgen belirtmiyor")






