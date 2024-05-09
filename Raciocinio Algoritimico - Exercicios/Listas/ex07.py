'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números'''
vetor = []
for i in range(5):
    inputzao = int(input(f'Digite o {i+1} valor!'))
    vetor.append(inputzao)
print(f'Os números são {vetor}')
print(f'A soma é: {sum(vetor)}')
mult = 1
for j in vetor:
    mult*= j
print(f'A multiplicação é {mult}')