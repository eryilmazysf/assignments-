n=int(input("Hangi sayıya kadar asal sayılar yazılsın: "))
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
