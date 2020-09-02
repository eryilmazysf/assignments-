from os.path import sep

print("yusuf\nsüheyl")  #  \n bir satır aşağı kaydırır
print("emin\t\tzehra")  # \t tab kadar boşluk bırakır

def sayılarıtopla(*args):  # def  fonksiyon oluşturma
 toplam=1
 for i in args:
  toplam *=i
 return toplam
print(sayılarıtopla(1,2,3,4))

print("ali","veli",49,50 ,sep='*' ,end='!!!!')  # sep='içine yazılanı aralara koyar '
print("alt satıra gecmeden devam et ünlem işareti koy") #  end='alt satıra gecmeden devam eder'
print(*"TBMM",sep='.')  #eger basına yıldız koyarsam ayrı ayrı yazar
print("{} + {} nin toplamı {} eder" .format(4,5,9))  #{} süslü parantez .format  ile değer ataması yapılabilir
print("%s takımı bu sene %s puanı var"%("bjk",45))  #  %s ifadesine hem string hem int deger ataması yapılabilir
