"""def ekok(sayı1,sayı2):
    if (sayı1>sayı2):
        sayı1,sayı2=sayı2,sayı1
    for x in range(sayı2,sayı1*sayı2+1,sayı2):
        if(x%sayı1==0):
            return x

sayı1=int(input("sayı1:"))
sayı2=int(input("sayı2:"))
print("{} ile {} ekoku={}".format(sayı1,sayı2,ekok(sayı1,sayı2)))
"""


def ekok_bulma(sayı1, sayı2):
    i = 2
    ekok = 1
    while True:
        if (sayı1 % i == 0 and sayı2 % i == 0):
            ekok *= i

            sayı1 //= i
            sayı2 //= i


        elif (sayı1 % i == 0 and sayı2 % i != 0):
            ekok *= i

            sayı1 //= i


        elif (sayı1 % i != 0 and sayı2 % i == 0):
            ekok *= i

            sayı2 //= i
        else:
            i += 1
        if (sayı1 == 1 and sayı2 == 1):
            break
    return ekok


sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ekok:", ekok_bulma(sayı1, sayı2))