def ebob(sayı1,sayı2):

    if (sayı1<sayı2):
        i=sayı1 #kucuk sayı için
    else:
        i=sayı2

    while (i>1):
        if(sayı1%i==0 and sayı2%i==0):
            return i
        i-=1

sayı1=int(input("sayı1:"))
sayı2=int(input("sayı2:"))
print("{} ile {} ebobu={}".format(sayı1,sayı2,ebob(sayı1,sayı2)))