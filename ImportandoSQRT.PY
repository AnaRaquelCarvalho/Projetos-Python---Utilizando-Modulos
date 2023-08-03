print('='*16, 'Importando Sqrt' ,'='*16)
from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}\n'.format(num,raiz))

print('='*12, 'Importando Sqrt e floor' ,'='*12)
from math import sqrt, floor
n1 = int(input('Digite um número: '))
raizQ = sqrt(n1)
print('A raiz de {} é igual a {}'.format(n1, floor(raizQ)))
print('='*50)