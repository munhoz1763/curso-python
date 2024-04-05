print('A confederação Nacional de Natação precisa saber a sua idade para descobrir sua categoria categoria')
idade = int(input('Por favor, digite a sua idade: '))
if idade <= 9:
    categoria = 'MIRIM'
elif idade >= 10 and idade <= 14:
    categoria = 'INFANTIL'
elif idade >= 15 and idade <= 19:
    categoria = 'JUNIOR'
elif idade == 20:
    categoria = 'SENIOR'
else:
    categoria = 'MASTER'
print('Com a idade de {} anos, voce está na categoria {}!'.format(idade, categoria))
