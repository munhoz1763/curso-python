largura = float(input('qual a largura da parede para pintar?: '))
altura = float(input('e qual a altura da parede?: '))
area = largura * altura
tinta = area / 2
print('a cada 2m² usa 1 litro de tinta, a quantidade necessaria para pintar essa parede de {}m² é {:.2f} litros de tinta'.format(area, tinta))