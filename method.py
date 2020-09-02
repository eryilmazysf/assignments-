class yazılımcı():
    def __init__(self,adı,soyadı,maas,diller,kurs):
        self.adı=adı
        self.soyadı=soyadı
        self.maas=maas
        self.diller=diller
        self.kurs=kurs
    def bilgilerigöster(self):
        print("""
        Adı:{}
        Soyadı:{}
        Maas:{}
        Bildigi_Diller:{}
        Aldıgı_kurslar:{}
        """.format(self.adı,self.soyadı,self.maas,self.diller,self.kurs))

    def zam_ekle(self,zam_miktarı):
        self.maas+=zam_miktarı

    def dil_ekle(self,yeni_dil):
        self.diller.append(yeni_dil)
    def kurs_ekle(self,yeni_kurs):
        self.kurs.append(yeni_kurs)


yazılımcı1= yazılımcı("yusuf","eryılmaz",5000,["python","java"],["javascript","html"])
yazılımcı1.bilgilerigöster()
yazılımcı1.dil_ekle("C++")
yazılımcı1.zam_ekle(250)
yazılımcı1.bilgilerigöster()