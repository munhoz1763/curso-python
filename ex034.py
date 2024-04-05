salario = float(input('Qual o seu salario para darmos o aumentos justo?: R$'))
if salario >= 1250:
    Novosalario = salario + salario * 10 / 100
    print('Com o aumento de 10%')
else:
    Novosalario = salario + salario * 15 / 100
    print('Com o aumento de 15%')
print('O seu novo salário é R${:.2f}'.format(Novosalario))