while True:  #sonsuz döngü
    name=str(input("your name (if you want to exit push q ):::"))
    if (name=="q"):
        print("wait to quit.....")
        break
    print("your name:",name)
i=0
while (i<10):
    print("i:",i)
    i+=1
    if (i==5):
        continue #continue eğer çalışırsa alttaki hiçbir şey çalışmaz başa döner
    else:
        print("i nin değeri:",i)

liste=list(range(12))
for i in liste:
    print(liste)
lstm=[(1,2,3),(4,5,6,7,8,9)]
listem=[1,2,3,4,5,6,7,8,9]
listem1=list()
for i in listem:
    listem1.append(i)
print(listem1)
listem2=[i for i in lstm ] #list comprahansion
print(listem2)
listem3=[x for i in lstm for x in i] #list comprahansion
print(listem3)






