#ALGORITIMO VERIFICADOR DO CPF
#Pedindo os digitos do CPF para o úsuario

d1 = int(input('Digito 1 '))
d2= int(input('Digito 2 '))
d3 = int(input('Digito 3 '))
d4 = int(input('Digito 4 '))
d5 = int(input('Digito 5 '))
d6 = int(input('Digito 6 '))
d7 = int(input('Digito 7 '))
d8 = int(input('Digito 8 '))
d9 = int(input('Digito 9 '))
#CALC DIGITO 1
calculo = d1* 10 + d2 * 9 + d3 * 8 + d4 * 7 + d5 * 6 + d6 * 5 + d7 * 4 + d8 * 3 + d9 * 2
digito1 = calculo * 10 % 11
if digito1 == 10:
    digito1 == 0
#CALC DIGITO 2
calculo2 = d1 * 11 + d2 * 10 + d3 * 9 + d4 * 8 + d5 * 7 + d6 * 6 + d7 * 5 + d8 * 4 + d9 * 3 + 2 * 2
digito2 = calculo2 * 10 % 11

print(f'Os digitos do CPF são: {d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}{d9}-{digito1}{digito2} ')