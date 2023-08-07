print('='*6, 'Ordem do Sorteio - Random e Shuffle ' ,'='*6)
import random
n1 = str(input('Nome: '))
n2 = str(input('Nome: '))
n3 = str(input('Nome: '))
n4 = str(input('Nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será :')
print(lista)

print('\n','='*6, 'Ordem dos Melhores Jogadores do século' ,'='*6)
from random import shuffle
jg1 = str(input('Nome: '))
jg2 = str(input('Nome: '))
jg3 = str(input('Nome: '))
jg4 = str(input('Nome: '))
jg5 = str(input('Nome: '))
list = [jg1, jg2, jg3, jg4, jg5]
shuffle(list)
print('Os melhores foram: ')
print(list)
print('='*54)
