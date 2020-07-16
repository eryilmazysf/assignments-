number=int(input('what is your limit to find the prime number:'))
prime=list()
for x in range(1, number + 1):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            prime.append(x)
print(prime)