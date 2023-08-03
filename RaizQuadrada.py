print('='*19, 'Raiz Quadrada' ,'='*19)
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}\n'.format(num, raiz))

print('='*8, 'Raiz Quadrada - Arredonda para cima', '='*8)
import math
n1 = int(input('Digite um número: '))
raizQ = math.sqrt(n1)
print('A raiz de {} é igual a {}\n'.format(n1, math.ceil(raizQ)))

print('='*8, 'Raiz Quadrada - Arredonda para baixo' ,'='*8)
import math
n = int(input('Digite um númerfo: '))
RaizQ = math.sqrt(n)
print('A raiz de {} é igual a {}'.format(n, math.floor(RaizQ)))
print('='*54)