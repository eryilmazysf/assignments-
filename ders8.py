toplam=0
list=(1,2,3,4,5,6,7,8,9)
for i in list:
    toplam=toplam+i
    if i%3==0:
        print(i)
print(toplam)
liste1=[(1,2,3),(4,5,6),(7,8,9)]
for (i,j,k) in liste1:
    if j%2==0:
        print(i,j,k)
dict={"model":"bmw","year":2001,}
for k in dict.values():
    print(k)
for m in dict.items():
    print(m)

a=0 #while döngüsü
toplam=0
while (a<10):
    print(a)
    toplam += a
    a+=3
print(toplam)
m=0
tplm=0
while(m<=20):
    if m%5==0:
        tplm+=m
    m+=1
print(tplm)
print(*range(20))
print(*range(0,26,5))
a=range(5,11)
for z in a:
    print(z)
t=range(0,10)
for c in t:
    print("*"*c)
g=range(10,0,-1)
for f in g:
    print("*"*f)







