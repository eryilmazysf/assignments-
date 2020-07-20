while True:
    print('to quit press q')
    year=(input('enter a year:'))
    if year=='q':
        print('quit......')
        break
    else:
        year=int(year)
        if year%4==0:
            if year%100==0 and year%400!=0:
                print(year,'is not a leap year')
            elif year%400==0 or year%4==0:
                print(year,'is a leap year')
        else:
            print(year,'is not a leap year')
