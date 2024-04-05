km = float(input('Qual a velocidade atual do carro?: '))
if km > 80:
    multa = (km - 80) * 7
    print('O senhor está sendo MULTADO, pois excedeu o limite de velocidade de 80km/h!!')
    print('Terá que pagar R${:.2f} de multa'.format(multa))
    print('Tente dirigir com mais segurança na proxima vez!!')
else:
    print('Tudo ok senhor, pode seguir viagem!!!')