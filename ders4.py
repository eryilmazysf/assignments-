dosya = open("kayıt.text", "w")  # dosya oluşturma işlemi "w" yaz çünkü string ifade yazmak için dosya içine
print("1=yusuf", file = dosya,flush=True)   #dosya içine yazılacaklar  ve file =dosya ismi
dosya.close() #eger flush=True yazarsam close yapmama gerek yok

sayilar = [x for x in range (1,100) if x%5 ==0]  #liste oluşturma yöntemi
print(*sayilar)

# * birden fazla parametre alması için yapılıyor

def goster(*args):
    for i in args:
        print(i)
goster(1,2,3,4)