'''1. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
final e o tempo calculado em segundos

massa = 10.0
segundos = 0

while massa >= 0.5:
    massa /= 2
    segundos += 50

print(f'Massa final: {massa}, Segundos decorridos: {segundos}')'''

'''2. Escreva um programa em Python que gera números entre 1000 e 1999 e mostra aqueles
que divididos por 11 dão resto 5.

print('Os numeros que divididos por 11 e dão resto 5 são:')
for i in range(1000,1999):
    if i % 11 ==5:
        print(f"{i}")'''

'''3. Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.'''

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
