n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print('seu primeiro nome é: {}'.format(nome [0]))
print('seu ultimo nome é: {}'.format(nome[(len(nome)-1)]))

