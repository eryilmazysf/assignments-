import random
print("""
*************************
DİCE SİMULATİON
*************************
do not forget dice number between 1 and 8
""")
x=int(input("how many dice you will use:"))
while (x<1 or x>8):   #for control whether valid or not
    print("not valid value try again")
    x = int(input("how many dice you will use:"))
y=int(input("number of rolls:"))
while (y<0):           #for control whether valid or not
    print("not valid try again:")
    y = int(input("number of rolls:"))

total_list=[]
for m in range(1,y+1):#for counting
    total = 0
    for n in range(1,x+1):
        random_number= random.randint(1,6)  # for appearance number we make random number
        print(n,".diece: ",random_number)
        total+=random_number
    total_list.append(total)
    print(m,".total",total)
print(total_list)






