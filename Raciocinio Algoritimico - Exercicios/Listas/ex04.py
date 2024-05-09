'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
consoantes'''

vetor = []
contador = 0
result = []
vogais = 'aeiou'
for _ in range(10):
    inputz = input(f'Digite o {int(_ + 1)} valor!')
    vetor.append(inputz)
for consoantes in vetor:
    if consoantes not in vogais:
        result.append(consoantes)
        contador += 1
print(f'Foram lidas {contador} consoantes, são elas: {result}')