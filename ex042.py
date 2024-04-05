print('-='* 21)
print('Analizador de Triângulo')
print('-='* 21)
t1 = float(input('Qual o cumprimento do primeiro segmento: '))
t2 = float(input('Qual o cumprimento do segundo segmento: '))
t3 = float(input('Qual o cumprimento do terceiro segmento: '))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os cumprimentos PODEM formar um triangulo', end=' ')
    if t1 == t2 and t2 == t3:
        print('EQUILATERO')
    elif t1 != t2 and t2 != t3 and t1 != t3:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os cumprimentos NAO PODEM forma um triangulo')
