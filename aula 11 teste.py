#primero modo de fazer
a = 2
b = 10
print('os valores são \033[34;41m {} \033[m e \033[31;46m {} \033[m'.format(a, b))
#segundo modo de fazer
nome = 'felipinho'
print(' ola {} {} {}'.format('\033[30;47m', nome, '\033[m'))
print('\033[31;44m', '|='*42, '\033[m')
name = 'luiz'
cores = {'limpa':'\033[m',
        'amarelo':'\033[33m',
         'verde':'\033[32m',
         'azul':'\033[34m',
         'pretoebranco':'\033[7;29m'}
print(' seu nome é {}{}{} né ?'.format(cores['azul'], name, cores['limpa']))
print('{} {} {}'.format(cores['pretoebranco'], '|=' * 42, cores['limpa']))

