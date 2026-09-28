frase = 'Curso de python'
'''
#Fatiamento de string
print(frase) #Curso de python
print(frase[7]) #e
print(frase[9:16]) #python     - Escreve os caracteres da posição 9 até a posição 15, ou seja, escreve de n até n-1
print(frase[0:16:2]) #Crod yhn - Igual ao exemplo acima com a diferença que é pulando de 2 em 2 casas
print(frase[:5]) #Curso        - Escreve os caracteres do inicio até a posição 4, ou seja, de do inicio até n-1
print(frase[9:]) #python       - Escreve os caracteres da posição 9 até o final, ou seja, escreve de n até final
print(frase[0::3]) #Csdph      - Escreve os caracteres de 0 até o final, pulando de 3 em 3 casas
'''

'''
#Analisar um string, ou seja, saber informações sobre ela
print(len(frase)) #15            - retorna o tamanho da string
print(frase.count('o')) #2       - conta quantas vezes a letra 'o' apareceu
print(frase.count('o', 0, 7)) #1 - conta quantas vezes a letra 'o' apareceu entre o intervalo de 0 até 6
print(frase.find('rso')) #2      - retorna a posição onde começa a string 'rso'
print(frase.find('Android')) #-1 - Retorna -1 porque a string 'Android' não existe dentro da string 'frase'
'Curso' in frase #True           - pergunta se a string 'Curso' existe dentro da string 'frase', se existir retorna True, caso contrário retorna False
'''

'''
#Transformação de string
print(frase.replace('python', 'Android')) #Curso de Android - Substitui a string 'python' pela string 'Android'
print(frase.upper()) #CURSO DE PYTHON                       - Transforma todas as letras da string em maiúsculas
print(frase.lower()) #curso de python                       - Transforma todas as letras da string em minúsculas
print(frase.capitalize()) #Curso de python                  - Transforma a primeira letra da string em maiúscula e as demais em minúsculas
print(frase.title()) #Curso De Python                       - Transforma a primeira letra de cada palavra da string em maiúscula e as demais em minúsculas

frase2 = '   Estutando python      '

print(frase2.strip()) #Estudando python                     - Remove os espaços inuteis do inicio e do final da string
print(frase2.rstrip()) #   Estutando python                 - Remove os espaços inuteis do final da string
print(frase2.lstrip()) #Estutando python                    - Remove os espaços inuteis do inicio da string
'''
#Divisão de string
print(frase.split()) #['Curso', 'de', 'python']     - Divide a string em uma lista de palavras, utilizando o espaço como separador
dividido = frase.split() #['Curso', 'de', 'python'] - Divide a string em uma lista de palavras, utilizando o espaço como separador
print(dividido[0]) #Curso                           - Acessa a primeira palavra da lista
print(dividido[0] [3]) #s                           - Acessa a quarta letra da primeira palavra da lista

#Junção de string
print('-'.join(frase)) #C-u-r-s-o- -d-e- -p-y-t-h-o-n - Junta os caracteres da string utilizando o caractere '-' como separador
print('-'.join(frase.split())) #Curso-de-python       - Junta as palavras da string utilizando o caractere '-' como separador, para isso é necessário dividir a string em uma lista de palavras utilizando o método split() antes de utilizar o método join()