nome = str(input('Qual seu nome ?'))
if nome == 'felipe':
    print('que nome bonito')
    print('bom dia {}'.format(nome))
elif nome == 'joao' or nome == 'luiz' or nome == 'matheus':
    print('bom dia, voce tem um nome bem diferente {}'.format(nome))
elif nome in 'ana luzia marcia silvana':
    print('voce tem um nome feminino {}'.format(nome))
else:
    print('tenha um otimo dia {}'.format(nome))
