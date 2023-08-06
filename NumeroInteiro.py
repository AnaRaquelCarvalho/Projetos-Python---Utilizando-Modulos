print('='*20, 'Número Inteiro - math e ceil' ,'='*20)
import math
num = float(input('Digite um número: '))
print('O número digitado foi {} e a sua porção inteira é {} \n'.format(num,math.ceil(num)))

print('='*20, 'Número Inteiro - math e Trunc' ,'='*20)
from math import trunc
n1 = float(input('Digite um número: '))
print('O valor Digitado foi {} e a sua porção inteira é {}\n'.format(n1, trunc(n1)))

print('='*23, 'Número Inteiro - com Int ','='*23)
n = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))
print('='*74)