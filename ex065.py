cont = media = soma = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    numero = int(input('digite um numero: '))
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('quer continuar? [S/N]: ')).upper().strip()[0]
media = cont / soma
print('voce digitou {} numeros e a media foi de {:.2f}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
