# Um professor quer sortear um dos seus quatro alunos para apagar o quadro
# Faça um programa que ajude ele, lendo o nome deles e escreendo o nome do escolhido

from random import choice
aluno1 = input('\nPrimeiro aluno: ') 
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
print(f'O escolhido foi o aluno {choice([aluno1, aluno2, aluno3, aluno4])}\n')