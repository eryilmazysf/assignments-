sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
a=1 #counter for horizontal
b=1 #counter for vertical
print('- - - - - - - - - - -')
for x in range(len(sudoku[0])):
    for i in sudoku[x]:
        print(i, end=' ')
        if a%3==0 and a%9!=0:
            print('|',end=' ')
        a +=1
    if b%3==0:
        print('\n'+'- - - - - - - - - - -', end=' ')
    b += 1
    print()
