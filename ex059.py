v1 = float(input('Informe um valor: '))
v2 = float(input('Informe outro valor: '))
print('O que você quer fazer com esses valores?')
print('[1] SOMAR')
print('[2] MULTIPLICAR')
print('[3] SABER QUAL O MAIOR ENTRE OS DOIS VALORES')
print('[4] NOVOS VALORES')
print('[5] SAIR DO PROGRAMA')
opcao = int(input('Informe o que deseja: '))
while opcao != 5:
    if opcao == 1:
        print('=' * 40)
        soma = v1 + v2
        print('A soma de {} mais {} é igual a {}'.format(v1, v2, soma))
        print('=' * 40)
        opcao = int(input('Quer resetar o programa digite [4] ou se deseja sair digite [5]: '))
    elif opcao == 2:
        print('=' * 40)
        mult = v1 * v2
        print('{} vezes {} é igual a {}'.format(v1, v2, mult))
        print('=' * 40)
        opcao = int(input('Quer resetar o programa digite [4] ou se deseja sair digite [5]: '))
    elif opcao == 3:
        if v1 > v2:
            print('=' * 40)
            print('O PRIMEIRO valor é maior sendo {} e o menor sendo o SEGUNDO valor {}'.format(v1, v2))
            print('=' * 40)
            opcao = int(input('Quer resetar o programa digite [4] ou se deseja sair digite [5]: '))
        if v1 == v2:
            print('=' * 40)
            print('Os valores são iguais!!, PRIMEIRO valor é {} e o SEGUNDO valor é {}'.format(v1, v2))
            print('=' * 40)
            opcao = int(input('Quer resetar o programa digite [4] ou se deseja sair digite [5]: '))
        if v2 > v1:
            print('=' * 40)
            print('O SEGUNDO valor é maior sendo {} e o menor sendo o PRIMEIRO valor {}'.format(v2, v1))
            print('=' * 40)
            opcao = int(input('Quer resetar o programa digite [4] ou se deseja sair digite [5]: '))
    elif opcao == 4:
        print('=' * 40)
        v1 = float(input('Digite um novo valor: '))
        v2 = float(input('Digite mais um novo valor: '))
        print('[1] SOMAR')
        print('[2] MULTIPLICAR')
        print('[3] SABER QUAL O MAIOR ENTRE OS DOIS VALORES')
        print('[4] NOVOS VALORES')
        print('[5] SAIR DO PROGRAMA')
        opcao = int(input('O que deseja fazer agora?: '))
        print('=' * 40)
    elif opcao == 5:
        print('Voce saiu')
    else:
        print('ERROO, TENTE NOVAMENTE')
        print('=' * 40)
        v1 = float(input('Digite um novo valor: '))
        v2 = float(input('Digite mais um novo valor: '))
        print('=' * 40)
        print('[1] SOMAR')
        print('[2] MULTIPLICAR')
        print('[3] SABER QUAL O MAIOR ENTRE OS DOIS VALORES')
        print('[4] NOVOS VALORES')
        print('[5] SAIR DO PROGRAMA')
        opcao = int(input('O que deseja fazer agora?: '))
        print('=' * 40)
print('-' * 40)
print('Voce saiu do programa, volte sempre!!!')
print('-' * 40)