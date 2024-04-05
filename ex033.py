n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
if (n1 < n2 and n3):
    Nmenor = n1
if (n2 < n1 and n3):
    Nmenor = n2
if (n3 < n1 and n2):
    Nmenor = n3
if (n1 > n2 and n3):
    Nmaior = n1
if (n2 > n1 and n3):
    Nmaior = n2
if (n3 > n1 and n2):
    Nmaior = n3
print('O menor numero digitado foi {}'.format(Nmenor))
print('O maior numero digitado foi {}'.format(Nmaior))