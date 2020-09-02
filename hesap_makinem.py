from math import*
print(""" 
 **********************
 HESAP MAKİNESİ
 1-)TOPLAMA
 2-)ÇIKARMA
 3-)BÖLME
 4-)ÇARPMA
 5-)ÜS ALMA
 6-)KAREKÖK ALMA
 7-)LOGARİTMA  
 ********************** 
       """
)
x=int(input("bir işlem seçiniz:"))
if (x==1):
    toplam=0
    y=int(input(("kaç sayı toplayacaksınız:")))
    while (y>0):
        print(y,"ıncı değeri giriniz...")
        a=int(input())
        toplam+=a
        y-=1
        print( toplam)

