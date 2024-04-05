km = float(input('quantos km voce andou com o carro?: '))
if km <= 200:
    multa = 5.50*km
    print('Voce vai ter que pagar R${:.2f} pela viagem de {}Km R$5,50 por litro'.format(multa, km))
else:
    multa = 6.00*km
    print('Voce vai ter que pagar R${:.2f} pela viagem de {}Km R$6,00 por litro'.format(multa, km))