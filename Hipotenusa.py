print('='*8, 'Hipotenusa - formula traducional e sem importação' ,'='*8)
n1 = float(input('Altura do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
hip = (n1 ** 2 + n2 ** 2) ** (1/2)
print(' A Hipotenusa vai medir: {:.2f}.\n'.format(hip))

print('='*16, 'Hipotenusa - Importando  math' ,'='*16)
import math
co = float(input('Altura do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = math.hypot(co, ca)
print('A Hipotenusa vai medir: {:.2f}.\n'.format(hipotenusa))

print('='*8, 'Hipotenusa - Método importa Hipotenusa ','='*8)
from math import hypot
num1 = float(input('Altura do Cateto Oposto: '))
num2 = float(input('Comprimento do Cateto Adjacente: '))
hi = hypot(num1, num2)
print('A Hipotenusa vai medir: {:.2f}.\n'.format(hi))
print('='*46)