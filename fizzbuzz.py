def fizzbuzz(x,y):
    for i in range(x,y+1):
        if (i % 15 == 0):
            print('FIZZBUZZ')
        elif(i%3==0):
            print('FIZZ')
        elif(i%5==0):
            print('BUZZ')
        else:
            print(i)
fizzbuzz(1,100)