n = s = cont = 0
while True:
    n = int(input('digite um numero: (999 faz ele parar)'))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foram o total de {cont} numeros, e a soma deles é {s}')
