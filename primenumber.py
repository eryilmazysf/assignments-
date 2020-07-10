while True:
    x=False
    number=input('please enter a number(to quit q):')
    if number=='q':
        print('quit......')
        break
    else:
        number = int(number)
        if (number<=0):
            x=True
        for i in range(2,number):
            if (number%i==0):
                x=True
        if (x or number==1):
            print('{} is not a prime number'.format(number))
        else:
            print('{} is a prime number'.format(number))

