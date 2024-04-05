cont = 0
soma = 0
for c in range(0, 6):
    n1 = int(input('digite um numero: '))
    if n1 % 2 == 0:
        soma = soma + n1
        cont += 1
print('Foram {} numeros PARES e o total foi de {}'.format(cont, soma))
