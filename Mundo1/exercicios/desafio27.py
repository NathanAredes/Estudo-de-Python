# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('\nDigite seu nome completo: ').strip().title()
dividido = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {dividido[0]}.')
print(f'Seu ultimo nome é {dividido[len(dividido)-1]}.\n')