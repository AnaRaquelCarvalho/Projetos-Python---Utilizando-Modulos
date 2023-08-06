print('='*6, 'Importando - Seno, Cosseno e Tangente ' ,'='*6)

from math import radians, sin, cos, tan
angulo = float(input('Digite o Ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem SENO de {:.2f}.'.format(angulo, seno))

Co = cos(radians(angulo))
print('O ângulo de {} tem COSSENO de {:.2f}.'.format(angulo, Co))

Ta = tan(radians(angulo))
print('O ângulo de {} tem TANGENTE de {:.2f}.\n'.format(angulo, Ta))

print('='*6, 'Seno, Cosseno e Tangente - Importando Math ' ,'='*6)
ang = float(input('Digite um ângulo: '))
import math
sen = math.sin(radians(ang))
print('O ângulo de {} tem Seno de {:.2f}.'.format(ang, sen))

Cossen = math.cos(radians(ang))
print('O ângulo de {} tem Cosseno de {:.2f}.'.format(ang, Cossen))

Tangen = math.tan(radians(ang))
print('O ângulo de {} tem Tangente de {:.2f}.'.format(ang, Tangen))
print('='*46)

