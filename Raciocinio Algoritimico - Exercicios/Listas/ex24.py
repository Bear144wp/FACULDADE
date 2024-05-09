'''Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em
um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma
 função para gerar numeros aleatórios, simulando os lançamentos dos dados.'''

from random import randint

contador = [0] * 6
for i in range(5):
    resultado = randint(1,6)
    contador[resultado - 1] += 1

print("Resultado: ")
for i in range(6):
    print(f'Valor {i+1} {contador[i]} vezes')
print(contador)