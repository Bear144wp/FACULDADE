'''10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''
vetor1 = []
vetor2 = []
vetor3 = []
for _ in range(10):
    input1 = input('Digite os primeiros 10 valores: ')
    vetor1.append(input1)
for _ in range(10):
    input2 = input('Digite os segundos 10 valores: ')
    vetor2.append(input2)

'''for k, y in zip(vetor1, vetor2):
    vetor3.append(k)
    vetor3.append(y)'''

for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(f'Os numeros das listas intercaladas é: {vetor3}')