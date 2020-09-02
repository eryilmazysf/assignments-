class harbiye():
    okulkomutanı="alpay"
    kurmaybaskanı="barbaros"
    def __init__(self,ders,komutan,bölüm="bilgiyok"):
        self.dersler=ders
        self.komutanlar=komutan
        self.bölümler=bölüm
alay=harbiye("ucus","kemal",bölüm="pilot")
dekanlık=harbiye("bilgisayar","mustafa",bölüm="piyade")
print(alay.okulkomutanı)
print(alay.dersler)
print(dekanlık.bölümler)
print(dekanlık.komutanlar)
ogrenci=harbiye("kültür","sedat")
print(ogrenci.kurmaybaskanı)
print(ogrenci.bölümler)




