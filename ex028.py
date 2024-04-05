from random import randint
from time import sleep
n1 = randint(0, 5)
n2 = int(input('Tente adivinhar o numero do Pc de 0 a 5: '))
print('O numero digitado é {}'.format(n2))
print('-=-' * 20)
print('PROCESANDO....')
sleep(2)
if n2 == n1:
    print('Parabens voce acertou o numero aleatorio!!')
else:
    print('Que pena voce errou o numero era o numero {}'.format(n1))
print('-=-' * 20)
