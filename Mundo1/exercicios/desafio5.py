# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))

down = num - 1
up = num + 1

print(f'Antecessor de {num} é {down} e o sucessor {up}')