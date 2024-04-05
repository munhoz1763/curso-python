from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa ''')
    opcao = int(input('Qual a sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
           maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor : '))
    elif opcao == 5:
        print('FINALIZANDO.....')
    else:
        print('Opção invalida... tente novamente')
    print('=-=' * 10)
    sleep(1135)
print('Fim do programa')