mylist=["345","asd","584a","15"]
for i in mylist:
    try:
        i=int(i);
        print(i);
    except:
        pass


def even(number):

        if (number % 2 == 0):
            return number
        else:
            raise ValueError("catch odd number")


liste = [34, 2, 1, 3, 33, 100, 61, 1800]

for i in liste:
    try:
        print(even(i));
    except ValueError:
        pass
