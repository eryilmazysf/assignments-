print("attending list")
i=1
x=int(input("enter class seize:"))
while i<=x:
    a =input("student name:")
    b =input("student id:")
    c =input("student class:")
    d = [a, b, c]  # listeye eleman ekleme
    print("student name:{}\n student id:{} \n student class:{} \n".format(d[0], d[1], d[2]))  # formatlama
    if i>x:
        break
    i+=1

