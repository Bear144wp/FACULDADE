'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''
vetor = []
for _ in range(5):
    inputzao = int(input('Digite o num: '))
    vetor.append(inputzao)
print(f'Os números são {vetor}')