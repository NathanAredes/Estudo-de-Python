# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math
num = float(input('\nDigite um número: '))
print(f'O ângulo de {num} tem o cosseno de {math.cos(math.radians(num)):.2f}')
print(f'O ângulo de {num} tem o seno de {math.sin(math.radians(num)):.2f}')
print(f'O ângulo de {num} tem o tangente de {math.tan(math.radians(num)):.2f}')