'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''
notas = []
for i in range(4):
    nota = int(input(f'Digite a {int(i + 1)} nota'))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f'As notas foram: {notas}, e a média é: {media}')