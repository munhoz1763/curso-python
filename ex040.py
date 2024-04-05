n1 = float(input('Qual foi a primeira nota?: '))
n2 = float(input('Qual foi a segunda nota?: '))
media = (n1 + n2) / 2
if media <= 5.0:
    print('Reprovado')
    print('Sua media foi de {:.1f}'.format(media))
elif media > 5.0 and media <= 6.9:
    print('Recuperação')
    print('Sua media foi de {:.1f}'.format(media))
elif media >= 7.0:
    print('Aprovado')
    print('Sua media foi de {:.1f}'.format(media))
    