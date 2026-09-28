# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

'''from math import trunc
num = float(input('\nDigite um número: '))
print(f'O número {num} pegando a parte inteira fica {trunc(num)}\n')'''

num = float(input('\nDigite um número: '))
print(f'O número {num} pegando a parte inteira fica {int(num)}\n')