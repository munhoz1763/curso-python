total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total de gastos é de R${total:.2fd}')
print(f'Temos {totmil} produtos custando mais de R$1000')
print(f'O produto mais barato é {barato} que custa R${menor:.2f} ')
