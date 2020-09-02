x="ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
f=dict()
for karakter in x:
    if (karakter in f):
        f[karakter]+=1
    else:
        f[karakter]=1
for i,j in f.items():
    print (i,":",j )

