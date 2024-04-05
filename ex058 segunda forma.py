from random import randint
computador = randint(0, 10)
print('Sou seu computador.... Estou pensando em um numero entre 0 e 10.')
print('Voce consegue acertar? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente')
        elif jogador > computador:
            print('Menos... tente novamente')
print('Acertou com {} tentativas, parabens!!'.format(palpites))
