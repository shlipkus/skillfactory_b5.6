game = True
count = 0
winer = ''
pole = [
    [' ', '0', '1', '2'],
    ['0', '-', '-','-'],
    ['1', '-', '-','-'],
    ['2', '-', '-','-']
]
combo = [
    [1, 1, 1, 2, 1, 3],
    [2, 1, 2, 2, 2, 3],
    [3, 1, 3, 2, 3, 3],
    [1, 1, 2, 1, 3, 1],
    [1, 2, 2, 2, 3, 2],
    [1, 3, 2, 3, 3, 3],
    [1, 1, 2, 2, 3, 3],
    [3, 1, 2, 2, 1, 3],
]
def hod(a):
    global game, winer, count
    x = int(input(f'Игрок {a} ваш ход! Введите номер строки: '))
    if x>=0 and x<=2:
        y = int(input(f'Игрок {a} ваш ход! Введите номер столбца: '))
        if y>=0 and y<=2 and pole[x+1][y+1] == '-':
            count += 1
            pole[x+1][y+1] = a
            for i in combo:
                if pole[i[0]][i[1]] == a and pole[i[2]][i[3]] == a and pole[i[4]][i[5]] == a:
                    winer = f"Победил {a}"
                    game = False
            if count >= 9:
                game = False
                winer = 'Ничья!'
            return
        else:
            print('Недопустимое значение')
            hod(a)
    else:
        print('Недопустимое значение')
        hod(a)

while game:
    for i in pole:
        print(*i)
    hod('X')
    for i in pole:
        print(*i)
    if game:
        hod('O')
print(winer)
