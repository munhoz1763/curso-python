from random import randint
v = 0
while True:
    jogador = int(input('Mostre um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Impar?[P/I]: ')).upper().strip()[0]
    print(f'Voce mostrou {jogador} e o computador mostrou {computador}, total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('Voce ganhou')
            v += 1
        else:
            print('Voce perdeu')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('Voce ganhou')
            v += 1
        else:
            print('Voce perdeu')
            break
    print('Vamos jogar novamente')
print(f'ACABOU O JOGO..... Voce ganhou {v} vezes')
