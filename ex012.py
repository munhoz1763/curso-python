produto = float(input('qual o preço do produto para ver o desconto:'))
desconto = (produto * 5) / 100
novopreco = produto - desconto
print('o preço do produto é R${:.2f} e com desconto de 5% fica no valor R${:.2f}'.format(produto, novopreco))