''' Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.'''

idade = []
altura = []
for i in range(5):
    idadizinha = int(input('Pessoa {}, Digite sua idade: '.format(i+1)))
    idade.append(idadizinha)
    alturazinha = int(input('Pessoa {}, Digite sua altura: '.format(i+1)))
    altura.append(alturazinha)
for j in range(4, -1, -1):
    print(f'A pessoa {j+1} tem altura: {altura[j]}, e idade: {idade[j]}')