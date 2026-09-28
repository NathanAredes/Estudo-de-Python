# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot
co = float(input('\nDigite o valor do cateto oposto: ')) 
ca = float(input('Digite o valor do cateto adjacente: '))
#hip = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
hip = hypot(co, ca)
print(f'A hipotenusa será {hip:.2f}\n')