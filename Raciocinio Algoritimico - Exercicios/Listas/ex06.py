'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0'''
medias = []
medias_altas = 0
for i in range(3):
    notas = []
    for j in range(4):
        inputzao = int(input(f'Aluno {int(i+1)}, digite sua nota {int(j+1)}:'))
        notas.append(inputzao)
    media_calc = sum(notas) / len(notas)
    medias.append(media_calc)
for k in medias:
    if k >= 7:
        medias_altas += 1
print(f'O número de alunos com a média maior ou igual a 7 é: {medias_altas}')