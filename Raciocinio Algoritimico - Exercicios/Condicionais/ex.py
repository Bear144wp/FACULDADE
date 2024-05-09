'''1. Tendo como dados de entrada a altura e o sexo de uma pessoa, implemente um
programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
• para homens: (72.7 * h) – 58;
• para mulheres: (62.1 * h) – 44.7.'''

'''altura = float(input('Digite sua altura (ex: 1.62): '))
sexo = input('Digite seu sexo M/F: ').upper()

if sexo == 'M':
    formula = (72.7 * altura) - 58
    print(f'Seu peso ideal é de {formula}')'''

'''2. O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde
para dar uma indicação sobre a condição de peso de uma pessoa adulta. A fórmula é IMC
= peso / altura2 . Implemente um programa que leia o peso e a altura de um adulto e mostre
sua condição de acordo com a tabela abaixo.
IMC em adultos Condição
• Abaixo de 18,5 – Abaixo do peso
• Entre 18,5 e 25 – Peso normal
• Entre 25 e 30 – Acima do peso
• Acima de 30 – Obeso

peso = float(input('Digite seu peso'))
altura = float(input('Digite sua altura (ex 1.62)'))
calculo = peso / (altura *2)

if calculo <= 18:
    print(f'Voce está abaixo do peso, seu imc é {calculo}')

elif calculo > 18.5 and calculo <= 25 :
    print(f'Voce está com peso normal, seu imc é {calculo}')

elif calculo > 25 and calculo < 30:
    print(f'Voce está acima do peso seu imc é {calculo}')

else:
    print(f'Voce está obeso seu imc é {calculo}')'''

''' 3. Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
rodada'''

while True:
    valores = list(range(1,6))
    jogador1 = int(input('Jogador 1, insira seu valor: '))
    if jogador1 not in valores:
        print('Números invalidos cadela, tente novamente de 1 a 5')
        continue
    palpite1 = input('Jogador 1, insira seu palpite: PAR ou IMPAR: ').lower()
    if 'par'or 'impar' not in palpite1:
        print('TENTE NOVAMENTE, VALORES ERRADOS')
        continue
    jogador2 = int(input('Jogador 2, insira seu valor: '))
        print('Números invalidos cadela, tente novamente de 1 a 5')
    palpite2 = input('Jogador 2, insira seu palpite: PAR ou IMPAR: ').lower()

    resultado = jogador1 + jogador2

    final = 'par' if resultado % 2 == 0 else 'impar'

    if final == palpite1 and final == palpite2:
        print('EMPATE CADELAS! ')
    elif final == palpite1:
        print(F'JOGADOR 1 VENCEU, O RESULTADO É {resultado}, e o número é {final}')
    elif final == palpite2:
        print(F'JOGADOR 2 VENCEU, O RESULTADO É {resultado}, e o número é {final}')

