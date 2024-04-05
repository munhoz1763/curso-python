peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual a sua altura?: '))
Imc = peso / (altura ** 2)
print('Seu Imc é {:.1f}'.format(Imc))
if Imc <= 18.5:
    print('Está abaixo do peso, melhore sua alimentação')
elif Imc > 18.5 and Imc <= 25:
    print('Parabens !! voce está no peso ideal, continue assim')
elif Imc > 25 and Imc <= 30:
    print('Voce esta com Sobrepeso, tome cuidado e melhore sua alimentação')
elif Imc > 30 and Imc <=40:
    print('Voce esta com Obesidade, voce esta em situação de perigo!!, isso pode causar inumeros problemas de saude')
else:
    print('Voce está em situação de Obesidade Morbida, voce está em perigo de morte')
