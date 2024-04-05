Vcasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos voce quer pagar? '))
parcelas = Vcasa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(Vcasa, anos), end=' ')
print('a prestação sera de R${:.2f}'.format(parcelas))
if parcelas <= minimo:
    print('Empréstimo foi CONCEDIDO!')
else:
    print('Emprestimo foi CANCELADO')
