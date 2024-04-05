frase = input('digite uma frase: ').upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print('a primeira vez que ela aparece é na posiçao {}'.format(frase.find('A')+1))
print('e a ultima que ela aparece é na posiçao {}'.format(frase.rfind('A')+1))