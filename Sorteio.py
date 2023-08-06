print('='*6, 'Sorteando - Com o módulo Random e Choice' ,'='*6)
n1 = str(input('Nome: '))
import random
n2 = str(input('Nome: '))
n3 = str(input('Nome: '))
n4 = str(input('Nome: '))
n5 = str(input('Nome: '))
n6 = str(input('Nome: '))
n7 = str(input('Nome: '))
n8 = str(input('Nome: '))
n9 = str(input('Nome: '))
lista = [n1, n2, n3, n4, n5, n6, n7, n8, n9]
print('O aluno escolhido foi o(a) {}\n'.format(random.choice(lista)))

print('='*16, 'Sorteando novamente','='*16)
n2 = str(input('Nome: '))
n3 = str(input('Nome: '))
n4 = str(input('Nome: '))
import random
Lista = [n1, n2, n3, n4]
escolhido = random.choice(Lista)
print('O escolhido foi {}\n'.format(escolhido))

print('='*16, 'Sorteando Novamente' ,'='*16)
from random import choice
n2 = str(input('Nome: '))
n3 = str(input('Nome: '))
n4 = str(input('Nome: '))
n4 = str(input('Nome: '))
list = [n1, n2, n3, n4,n5]
print('O escolhido foi {}'.format(choice(list)))
