masculino = 0
feminino = 0
total18 = 0
while True:
        print('-' * 30)
        idade = int(input('Idade: '))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo: [F/M] ')).upper().strip()[0]
            print('-' * 30)
        if idade >= 18:
                total18 += 1
        if sexo == 'M':
                masculino += 1
        if sexo == 'F' and idade < 20:
                feminino += 1
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp == 'N':
            break
print(f'TOTAL DE PESSOAS COM 18 ANOS É: {total18}')
print(f'AO TODO TEMOS {masculino} HOMENS CADASTRADOS')
print(f'E TEMOS {feminino} MULHER COM MENOS DE 20 ANOS')

