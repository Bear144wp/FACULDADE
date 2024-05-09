'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

media_temp = []
meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
for i in range(12):
    inputzao = int(input((f'Insira a temp média do mes {meses[i]} (em graus celcius): ')))
    media_temp.append(inputzao)
media_anual = sum(media_temp) / len(media_temp)
print(f'A média anual é: {media_anual}')
for j in range(12):
    if media_temp[j] > media_anual:
        print(f'{meses[j]} - {media_temp[j]}')