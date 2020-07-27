def lucky_sum(*numbers):
    x=list()
    total=0
    for i in numbers:
        x.append(i)

    if 13 in x:
        for i in range(x.index(13)):
            total+=x[i]
        print(total)
    else:
        for i in range(len(x)):
            total+=x[i]
        print(total)

lucky_sum(1,2,3,4,13,5)  #just sum left side of 13