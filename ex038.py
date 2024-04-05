pValor = int(input('digite o primeiro numero: '))
sValor = int(input('digite o segundo numero: '))
if pValor > sValor:
    print('O primeiro valor {} é maior'.format(pValor))
elif sValor > pValor:
    print('O segundo valor {} é maior'.format(sValor))
else:
    print('Não existe valor maior, os dois são iguais')