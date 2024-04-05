num = int(input('Digite um numero inteiro: '))
print(''' Escolha uma das opçoes abaixo para converter:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O numero {} em BINARIO é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O numero {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O numero {} em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida')