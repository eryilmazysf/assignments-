from functools import reduce
list1=[1,2,3]
list2=[4,5,6]
print(list(map(lambda x,y:x**y,list1,list2))) ##
def double(x):
    x=x**2
    return x
print(list(map(double,list1 )))



print(reduce(lambda x,y:x*y,[1,2,3]))  ##map fonk ile aynı sadece iki iki alarak işlem yapıyor
def max(x,y):
    if (x>y):
        return x
    else:
        return y
print(reduce(max,[-1,-8,4,8,-5,1]))
print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8]))) #filter ilk değer boolean olmak zorunda
sozluk1={"elma":"apple","kırmızı":"red"}
sozluk2={"one":1,"two":2}



print(list(zip(sozluk1,sozluk2.values()))) #zip ile birleştirme yapılır iki liste

listem1=["java","python","c++"]
listem2=[1,2,3]
listem3=[]
for a,b in zip(listem1,listem2):
    listem3.append([a,b])
print(listem3)



listem=[]
for i,j in enumerate(listem1): #enumerate ile index ve eleman olarak yazdırabiliriz
    listem.append((i,j))
print(listem)

listeler=[True,False,True,True];
print(all(listeler)) #and olarak islem yapar
print(any(listeler)) # or olarak islem yapar


def alanhesapla(x):
    return x[0]*x[1]

dikdörtgen=[(3,4),(10,3),(5,6),(1,9)];
print(list(map(alanhesapla,dikdörtgen)))

def ucgentest(y):
    if (y[0]+y[2]>y[1]>abs(y[2]-y[0])):
        return True
    else :
        return False

ucgen= [(3, 4, 5), (6, 8, 10),(6,4,10)];
print(list(filter(ucgentest,ucgen)))



numbers=[1,2,3,4,5,6,7,8,9,10];
filtre=list(filter(lambda x:x%2==0,numbers))
print(filtre)
print(reduce(lambda x,y:x+y,filtre))



name=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"];
lastname=["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"];
for i,j in zip(name,lastname):
    print(i,j)