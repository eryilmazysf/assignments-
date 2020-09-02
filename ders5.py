liste=[1,2,3,4,5,6,7,8,9,"yusuf"] #liste oluşturma
print(liste)
bos_liste=list() #boş liste oluşturma metodu
print(bos_liste)
liste[0]=15 #listedeki değeri değiştirme
print(liste)
text="I live in Canada"
liste1=list(text)
print(liste1) #string ifadeyi listeleme metodu
metin=""
for i in liste1:
    metin+=i
print(metin)
yeni_liste=liste[1:3]
print(yeni_liste)
liste_5=[1,2,3]
liste_6=[4,5,6]
liste_7=liste_5+liste_6+["süheyl"] #liste birleştirme ve listeye eleman ekleme
print(liste_7)
liste.append(55) #listeye eleman ekleme
liste.pop(0) #listeden eleman çıkarma
print(liste)
print(liste[5])
liste_sıralama=[58,46,505,2,85,75,23,105,1]
liste_sıralama.sort() #küçükten büyüğe sıralama
print(liste_sıralama)
liste_sıralama.sort(reverse=True)
print(liste_sıralama) #büyükten küçüğe sıralama
liste_liste=[[1,2,3],[4,5,6],[7,8,9]]
print(liste_liste[0][2]) #liste içinde liste oluşturduğumuzda listeden eleman çekme metodu