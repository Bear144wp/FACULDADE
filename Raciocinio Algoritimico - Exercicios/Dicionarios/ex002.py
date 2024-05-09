ano_luz = {
"pc": 0.31,
"al": 1,
"ae": 63241.09,
"ml": 525960.23,
"sl": 31557609.92
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]
print('Conversões disponiveis:')
for unidade in unidades:
    print(unidade)
print('-' *20)
valor = int(input('Digite o valor que deseja converter! '))
de = input('Converter de: ')
para = input('Converter para: ')
print('-' *20)

if de in ano_luz and para in ano_luz:
    conversao = valor * (ano_luz[de] * ano_luz[para])
    print(f'A conversão do valor {valor}, de origem {de}, para {para}, é: {conversao}')
else:
    print('Algo deu errado!')