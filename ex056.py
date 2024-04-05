idademaior = 0
nomevelho = ''
somamedia = 0
mulhermenor = 0
media = 0
for p in range(1, 5):
    print('-----{}ºPESSOA------'.format(p))
    nomes = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media = media + idade
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    if p == 1 and sexo == 'M':
        idademaior = idade
        nomevelho = nomes
    else:
        if idade > idademaior and sexo == 'M':
            idademaior = idade
            nomevelho = nomes
somamedia = media/4
print('A media de idade do grupo é de {} anos'.format(somamedia))
print('O homem mais velho tem {} anos e seu nome é {}'.format(idademaior, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulhermenor))
