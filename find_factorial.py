print("""
**************************
FİND MY FACTORİAL VALUE

to quit enter "q"
**************************
""")

while True:
    number=int(input("please enter number to find fatorial value:"))
    if number=="q":
        print("see you")
        break
    factorial = 1
    for i in range(2,number+1):
            factorial*=i

    print(factorial)

