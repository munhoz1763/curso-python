n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
dI = n1 // n2
ex = n1 ** n2
ds = n1 % n2
print('o valor da soma é {}, a multiplicação é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('a divisao inteira é {} e a exponenciaçao é {}'.format(dI, ex), end=' ')
print(' a sobra dos valores é {}'.format(ds))

