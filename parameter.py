def show_information(x,y):
    return x,y
i=1
while (i<2):
    name = input("name:")
    id = input("id:")
    i+=1
    print(show_information(name,id))




def knowledge(a="noname",b="no_id"):
    print("ad:",a,"id:",b)
knowledge("yusuf")      #id girişi yapmadık no_id olarak gördük
knowledge(b=123456)

def addition(*a):
    toplam=0
    for i in a:
        toplam+=i
    print(toplam)
    return toplam
addition(5,6,9)


