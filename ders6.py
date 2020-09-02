sözlük={"tree":"agac","book":"kitap","fredoom":"ozgurluk"} #sözlük olusturma
print(sözlük["tree"])
sözlük1=dict()
sözlük2={"üniversite":{"department":["dep1","dep2","dep3"]},"iş":{"mühendis":["computer","electronic"],"maraba":["amele1","amele2"]}}
print(sözlük2["iş"]["maraba"])
print(sözlük2["iş"].keys())
print(sözlük2["iş"].values())
print(sözlük.items())
"""a=int(input("bir sayı giriniz:"))
b=float(input("bir ondalık sayı giriniz:"))
print("çarpım:"+str(a*b))"""
x=int(input("doğum yılınızı giriniz:"))
y=int(2019-x)
print("yaşınız",y)
