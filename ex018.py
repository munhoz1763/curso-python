from math import sin, cos, tan, radians
angulo = float(input('digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('o angulo digitado é {} e o seno dele é {:.2f}'.format(angulo, seno))
coss = cos(radians(angulo))
print('o angulo digitado é {} e o cosseno dele é {:.2f}'.format(angulo, coss))
tang = tan(radians(angulo))
print('o angulo digitado é {} e a tangente dele é {:.2f}'.format(angulo, tang))
