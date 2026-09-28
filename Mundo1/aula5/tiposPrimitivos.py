'''
Tipos Primitivos em Python

int para números inteiros
float para números decimais
bool para valores booleanos 
str para texto, para ser texto precisa estar entre aspas.
'''


# A função type() é usada para verificar o tipo de dado de uma variável.
nInt = int(101)
nFloat = float(10.5)
vBool = bool(True)
textStr = str('Olá, mundo!')
print('Número inteiro:', type(nInt))
print('Número decimal:', type(nFloat))
print('Valor booleano:', type(vBool))
print('Texto:', type(textStr))


nome = input('\nInforme seu nome: ')
print('Ola {}, seja bem-vindo! {}'.format(nome, nome))
# O método .format() é usado para formatar strings, substituindo os {} pelo valor da variável nome.


num = input('\nDigite um número: ')
print('O número digitado é numérico?', num.isnumeric())
# O método .isnumeric() é usado para verificar se a string é composta apenas por números e retorna True ou False.


char = input('\nDigite um caractere: ')
print('O caractere digitado é alfabético?', char.isalpha())
# O método .isalpha() é usado para verificar se a string é composta apenas por letras e retorna True ou False.


char = input('\nDigite um caractere: ')
print('O caractere digitado é alfanumérico?', char.isalnum())
# O método .isalnum() é usado para verificar se a string é composta por letras e números e retorna True ou False.