def not_hesapla(satır):
    liste = satır.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])
    return isim,not1,not2,not3

with open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/notlar.txt", "r", encoding="utf-8") as file:
   liste = []
   for i in file:
       liste.append(not_hesapla(i))
   print(liste)




