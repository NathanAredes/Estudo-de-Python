# Cria um programa que leia o nome completo de uma pessoa a mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('\nDigite seu nome completo: ').strip()
print(f'Seu nome em maiúsculo: {nome.upper()}')
print(f'Seu nome em minúsculo: {nome.lower()}')
print(f'Seu nome tem o total de {len(nome) - nome.count(' ')} letras')
n = nome.find(' ')
print(f'Seu primeiro nome é {nome[:n]} e tem {nome.count('',0, n-1)} letras\n')