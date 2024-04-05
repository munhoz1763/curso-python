from random import randint
from time import sleep
errados = 0
computador = randint(0, 10)
jogador = int(input('Tente adivinhar o numero do Pc de 0 a 10: '))
while jogador != computador:
    print('=' * 40)
    print('O numero digitado é {}'.format(jogador))
    print('PROCESANDO....')
    print('=' * 40)
    sleep(0.5)
    if jogador != computador:
        errados += 1
        jogador = int(input('Voce errou, tente novamente: '))
    if jogador == computador:
            print('Parabens voce acertou!!')
print('Voce precisou errar {} vezes para adivinhar o numero do computador, que é o numero {}'.format(errados, computador))
