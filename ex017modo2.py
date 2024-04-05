import math
cateto1 = float(input('digite o cateto 1 : '))
cateto2 = float(input('digite o cateto 2 : '))
hipotenusa = math.sqrt(cateto1*cateto1 + cateto2*cateto2)
print("A hipotenusa é {:.2f}".format(hipotenusa))
