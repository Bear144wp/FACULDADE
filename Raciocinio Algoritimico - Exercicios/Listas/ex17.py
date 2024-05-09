'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco
distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O
programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme
o exemplo abaixo:'''

while True:
    nome = input('Digite seu nome: ')
    if nome == '':
        print('Finish')
        break

    saltos = []
    for i in range(5):
        inputz = float(input(f'Digite seu {i+1} salto: '))
        saltos.append(inputz)
    media = sum(saltos) / len(saltos)

    print('Atleta: ',nome)
    for j in range(5):
        print(f'{j+1} Salto = {saltos[j]}')
    print(f'Resultado final: \n Atleta: {nome} \n Saltos: {saltos}, Media dos saltos: {media}')