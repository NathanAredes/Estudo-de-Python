# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('\nDigite seu nome completo: ').strip()
print(f'Seu nome tem Silva? {'Silva' in nome.title()}\n')