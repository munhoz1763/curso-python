soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A quantidade numeros divisiveis por 3 é {} e a soma total deles é {}'.format(cont, soma))
