print(' GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    c += 1
print('fim')
