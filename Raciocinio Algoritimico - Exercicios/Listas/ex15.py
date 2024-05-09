'''15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem'''

values = []
while True:
    inputz = int(input('Digite o valor: '))
    if inputz == -1:
        break
    else:
        values.append(inputz)

a = len(values)
b = values
c = values[::-1]
d = sum(values)
e = sum(values) / len(values)

f = 0
for w in values:
    if w > e:
        f+=1

g = 0
for k in values:
    if k < 7:
        g += 1

print('a = {} b = {} c = {} d = {} e = {} f = {} g = {}'.format(a, b, c, d, e, f, g))


