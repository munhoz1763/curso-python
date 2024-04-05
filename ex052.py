numero = int(input('digite um numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi dividido {} vezes'.format(numero, tot))
if tot == 2:
    print('Ele é um número PRIMO')
else:
    print('Ele NÃO é um número PRIMO')
