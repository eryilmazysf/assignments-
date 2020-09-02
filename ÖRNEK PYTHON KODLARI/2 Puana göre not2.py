while True:
    puan = int(input("ORTALAMANIZI YAZINIZ\t: "))

    if puan<0 or puan>100:
        print("GEÇERLİ BİR NOT GİRİNİZ")
    elif puan<50 :
        print("BİR")
    elif puan<=59 :
        print("İKİ")
    elif puan<=69 :
        print("ÜÇ")
    elif puan<=84 :
        print("DÖRT")
    elif puan<=100 :
        print("BEŞ")


