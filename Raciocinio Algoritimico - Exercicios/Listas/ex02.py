'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''

vetor = []
for i in range(10):
    intpuz = int(input(f'Digite o {i + 1} número: '))
    vetor.append(intpuz)
print(f'Os números em ordem inversa é: {vetor[::-1]}')