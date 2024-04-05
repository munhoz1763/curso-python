n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
