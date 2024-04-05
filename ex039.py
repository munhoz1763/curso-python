from datetime import date
anoNasc = int(input('Em que ano voce nasceu?: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
if idade < 18:
    anos = 18 - idade
    print('Voce ainda vai se alistar algum dia')
    print('faltam {} anos'.format(anos))
    print('Seu alistamento é em {}'.format(anoNasc + 18))
elif idade == 18:
    print('É hora de se alistar')
else:
    anos = idade - 18
    print('Ja passou {} anos do tempo de se alistar'.format(anos))
    print('Era para ter se alistado em {}'.format(anoNasc + 18))
