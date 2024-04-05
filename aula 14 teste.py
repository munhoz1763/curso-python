totpar = 0
totimpar = 0
c = 1
while c != 0:
    c = int(input('digite um numero: '))
    if c % 2 == 0:
        totpar += 1
    else:
        totimpar += 1
print('total de numeros pares são {} e total de numeros impares sao {}'.format(totpar, totimpar))
