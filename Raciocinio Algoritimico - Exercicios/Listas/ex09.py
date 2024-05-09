'''9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
elementos do vetor.'''
lista = []
for i in range(3):
    inputzao = int(input(f'Digite o {i+1} num: '))
    lista.append(inputzao)
calc = 0
for j in lista:
    calc = j**2
    calc += calc
print(calc)