dias = int(input('quantos dias voce alugou o carro?: '))
km = float(input('quantos km o carro percorreu?: '))
total = (dias * 60) + (km * 0.15)
print('o total a pagar é : R${:.2f}'.format(total))