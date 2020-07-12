a=1
b=1
x=int(input("what do you want fibonacci value:"))
c=range(x)
fibonacci=[a]
for i in c:
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci)
