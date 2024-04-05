from math import hypot
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adja: '))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))
