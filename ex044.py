precoproduto = float(input('Qual o valor do produto?: '))
print('--' * 40)
print('''Formas de pagamento são:
[ 1 ] Dinheiro/Cheque, para 10% de desconto
[ 2 ] Cartao, para 5% de desconto
[ 3 ] Cartao em 2 vezes, para preço normal
[ 4 ] Cartao em 3 vezes ou mais, para 20% de juros''')
print('--' * 40)
pagamento = int(input('Qual a forma de pagamento?: '))
if pagamento == 1:
    novopreco = precoproduto - (precoproduto * 10 / 100)
    print('Como é pago em dinheiro ou cheque, o valor a ser pago é de R${:.2f}'.format(novopreco))
elif pagamento == 2:
    novopreco = precoproduto - (precoproduto * 5 / 100)
    print('Como é pago a vista no cartão, o valor a ser pago é de R${:.2f}'.format(novopreco))
elif pagamento == 3:
    print('Em ate 2x de R${:.2f}'.format(precoproduto / 2))
elif pagamento == 4:
    novopreco = precoproduto + (precoproduto * 20 / 100)
    parcelas = int(input('Em quantas parcelas?: '))
    print('O valor a ser pago em {}x de R${:.2f} COM JUROS'.format(parcelas, (novopreco / parcelas)))
    print('O total a ser pago é de {:.2f}'.format(novopreco))
else:
    print('Opção invalida, tente novamente!')


