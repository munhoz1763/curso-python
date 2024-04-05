import math
catetop = float(input('qual o cumprimento do cateto oposto: '))
catetoadj = float(input('qual o cumprimento do cateto adjacente: '))
catetop = pow(catetop, 2)
catetoadj = pow(catetoadj, 2)
hipotenusa = math.sqrt(catetop + catetoadj)
print('o cumprimento da hipotenusa é {:.2f}'.format(hipotenusa))
