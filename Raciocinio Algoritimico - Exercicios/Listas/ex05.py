'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''
par = []
impar = []
for i in range(20):
    leitura = int(input(f'Digite o {int(i + 1)} valor!'))
    if leitura % 2 ==0:
        par.append(leitura)
    else:
        impar.append(leitura)
print(f'Os números pares são: {par}, e os números impares são {impar}')