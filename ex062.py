print(' GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        c += 1
    print('pausa')
    mais = int(input('quantos termos voce quer a mais?: ').format(mais))
print('fim')
print('progrssão finalizada com {} temos'.format(total))
