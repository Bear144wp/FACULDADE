'''12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos.
'''
#Definindo variaveis "universais"
idade = []
altura = []
range_universal = 3

for i in range(range_universal):
    for j in range(1):
        idadis = int(input(f'{i+1} - Digite sua idade'))
        idade.append(idadis)
        alturis = int(input(f'{i+1} - Digite sua altura'))
        altura.append(alturis)
''' 
USAR ISSO CONSIDERANDO QUE: QUERO A MÉDIA DAS ALTURAS ACIMA DE 13 ANOS! NÃO A MÉDIA DE ALTURAS REFERENTE A TODAS AS IDADES!
soma_altura = []
for k in range(range_universal):
    if idade[k] > 13:
        soma_altura.append(altura[k])
media_altura = sum(soma_altura) / len(soma_altura)
'''
media_altura_universal = sum(altura) / len(altura)
contador = 0
for j in range(range_universal):
    if idade[j] > 13 and altura[j] < media_altura_universal:
        contador += 1
print(f'O número de alunos com mais de 13 anos e altura inferior a media é: {contador}')