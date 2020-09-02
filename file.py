file = open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt","w",encoding="utf-8")
file.write("yusuf\n")
file.close()
file = open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt","a",encoding="utf-8")
file.write("yasin \n")
file.write("ayse\n")
file.close()
file = open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt","r",encoding="utf-8")
for i in file:
    print(i,end="") #print fonksiyonu kendi \n koyar bunu önlemek için end parametresi koyarız
file.close()
file = open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt","a",encoding="utf-8")
file.write("emin\n")
file.write("zehra\n")
file.close()
file = open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt","r",encoding="utf-8")
icerik=file.read()
print(icerik)
file.close()
file = open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt","r",encoding="utf-8")
print("first line:",file.readline())
file.close()
file = open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt","r",encoding="utf-8")
list=file.readlines()
print(list)
file.close()
with open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt","r",encoding="utf-8") as file :
    print(file.tell())
    file.seek(5)
    print(file.read(8))
    file.seek(0)
with open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt", "a", encoding="utf-8") as file:
    print(file.tell())
    file.write("eryilmaz\n")
    print(file.tell())
with open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt", "r", encoding="utf-8") as file:
    print(file.read())
with open("C:/Users/ERYILMAZ/PycharmProjects/yusuf/ders/bilgiler.txt", "r+", encoding="utf-8") as file:
    liste=file.readlines()
    liste.insert(3,"suheyl\n")
    print(liste)
    for i in liste:
        print(i)













