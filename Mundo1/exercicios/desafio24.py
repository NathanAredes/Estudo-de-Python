# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nome = input('\nDigite da cidade: ').strip()
print(nome[:5].title() == 'Santo')