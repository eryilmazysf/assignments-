print("kütle indeksi hesaplama")
h=float(input("please enter your height:"))
w=int(input("please enter your weight:"))
index=float(w/(h*h))
print("your weight height index:",format(index))
if index>25:
    print("you are obese")

