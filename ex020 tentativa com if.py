import random
a1 = input('digite o nome do primeiro aluno: ')
a2 = input('digite o nome do segundo aluno: ')
a3 = input('digite o nome do terceiro aluno: ')
a4 = input('digite o nome do quarto aluno: ')
lista = (a1, a2, a3, a4)
print('--------------------------------------')
print('os alunos a serem sorteados são', lista)
print('--------------------------------------')
sorteado1 = random.choice(lista)
sorteado2 = random.choice(lista)
sorteado3 = random.choice(lista)
sorteado4 = random.choice(lista)
if sorteado2 == sorteado1:
        sorteado2 = random.choice(lista)
if sorteado3 == (sorteado1 and sorteado2):
        sorteado3 = random.choice(lista)
if sorteado4 == (sorteado1 and sorteado2 and sorteado3):
        sorteado4 = random.choice(lista)
print('o primeiro aluno a apresentar será {}'.format(sorteado1))
print('o segundo aluno a apresentar será {}'.format(sorteado2))
print('o terceiro aluno a apresentar será {}'.format(sorteado3))
print('o ultimo aluno a apresentar será {}'.format(sorteado4))