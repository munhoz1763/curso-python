while True:
    n = int(input('Quer ver a tabuada de qual numero? '))
    if n < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 20)
print('encerrada a tabuada')