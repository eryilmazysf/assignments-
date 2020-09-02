for i in range(1,11):
    print("**********")
    for j in range(1,11):
        print("{}*{}={}".format(i,j,i*j))


i=1
sum=0
print("to quit push q ")
while True:
    number = input("enter a number:")
    if(number=="q"):
        break
    number=int(number)
    sum+=number
    print(i, ".number:", number)
    i+=1

print("total value of your enter numbers:",sum)


