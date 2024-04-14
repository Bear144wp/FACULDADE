'''1. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
final e o tempo calculado em segundos

massa = 10.0
segundos = 0
while massa >= 0.5:
    massa /= 2
    segundos += 50
print(f'Massa final: {massa}, Segundos decorridos: {segundos}')



2. Escreva um programa em Python que gera números entre 1000 e 1999 e mostra aqueles
que divididos por 11 dão resto 5.

print('Os numeros que divididos por 11 e dão resto 5 são:')
for i in range(1000,1999):
    if i % 11 ==5:
        print(f"{i}")



3. Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.

jogadas = int(input('Digite o númmero de jogadas necessárias para finalizar o jogo: '))
i = 0
while i <= jogadas:
    jogador1 = int(input('Jogador 1, escolha:\n 1 - Pedra\n 2- Papel\n 3 - Tesoura'))
    jogador2 = int(input('Jogador 2, escolha:\n 1 - Pedra\n 2- Papel\n 3 - Tesoura'))
    #Opções 
    if jogador1 == 1 and jogador2 == 2: print('Jogador 2 ganhou')
    i += 1
    if jogador1 == 2 and jogador2 == 1: print('Jogador 1 ganhou')
    i += 1


4- Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente.

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
num4 = int(input('Digite o 4º número: '))
num5 = int(input('Digite o 5º número: '))
for _ in range(5):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num3 > num4:
        num3, num4 = num4, num3
    if num4 > num5:
        num4, num5 = num5, num4
print("Os números em ordem crescente são:")
print(num1, num2, num3, num4, num5)



5. Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
tempo necessário para que a população do país A ultrapasse a população do país B

paisA = 5000000
taxapaisA = 3/100
paisB = 7000000
taxapaisB = 2/100
contador = 0
while paisA <= paisB:
    paisA *= 1 + taxapaisA
    paisB *= 1 + taxapaisB
    contador += 1
print(f'Levara {contador} para a pop A ultapassar a pop B')



6. Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome.

n = str(input('Digite seu nome completo: '))
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))



7. Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
conjunto de palavras

counter_a = 0
while True:
    v1 = input('Digite a palavra:\n Para parar, digite enter')
    if 'a' in v1 or 'A' in v1:
        counter_a += 1
    if v1 == '':
        print(f'Finalizando...\n Existem {counter_a} letras A')
        break



8. Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal..

binario = input('Digite o número em binario para converter para decimal: ')
decimal = int(binario, 2)
print(f'O número binário {binario} em decimal é {decimal}')

9 - Elaborar um programa em Python que converta um número decimal em hexadecimal,
fazendo uso do método de divisões sucessivas.

decimal = int(input('Digite um número em decimal para transformar para hexa'))
hexa = int(decimal / 16)
if hexa ==10:
    hexa = 'A'
if hexa ==11:
    hexa = 'B'
if hexa ==12:
    hexa = 'C'
if hexa ==13:
    hexa = 'D'
if hexa ==14:
    hexa = 'E'
if hexa ==15:
    hexa = 'F'
hexa1 = decimal % 16
if hexa1 == 10:
    hexa1 = 'A'
if hexa1 == 11:
    hexa1 = 'B'
if hexa1 == 12:
    hexa1 = 'C'
if hexa1 == 13:
    hexa1 = 'D'
if hexa1 == 14:
    hexa1 = 'E'
if hexa1 == 15:
    hexa1 = 'F'
print(hexa, hexa1)


10. Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
consideração os anos bissextos).


import datetime
try:
    data1_str = input("Digite a primeira data (formato: DD/MM/AAAA): ")
    data2_str = input("Digite a segunda data (formato: DD/MM/AAAA): ")
    #vms transformar com o .striptime do datetime
    data1 = datetime.datetime.strptime(data1_str, "%d/%m/%Y")
    data2 = datetime.datetime.strptime(data2_str, "%d/%m/%Y")
    #vms verificar qual data é maior
    if data1 > data2:
        data_maior = data1
        data_menor = data2
    else:
        data_maior = data2
        data_menor = data1
    #subtração
    diferenca = data_maior - data_menor
    #result bro!
    print("A diferença entre as datas é de", diferenca.days, "dias.")
except:
    print('Ocorreu algum erro! Talvez você digitou no formato errado!\n'
          'Use as "/" para separar, não esqueça!')
'''
