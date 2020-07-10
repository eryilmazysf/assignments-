while True:
    x=False
    number=input('please enter a number(to quit q):')
    if number=='q':
        print('quit......')
        break
    else:
        number=int(number)
        if number==1:
            print('1 is not a prime number')
        elif number==2:
            print('2 is a prime number')

        for i in range(2,number):
            if (number%i==0):
                x=True
        if (x):
                print('{} is not a prime number'.format(number))
        else:
                print('{} is  a prime number'.format(number))

