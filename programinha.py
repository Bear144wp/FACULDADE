#qual letra apareceu mais?

quantidade = 0
letra = ''
frase = input('Digite um frase, e descubra qual letra apareceu mais! ')
for i in frase:
    if i == ' ':
        continue
    quantidade_apareceu = frase.count(i)
    if quantidade < quantidade_apareceu:
        quantidade = quantidade_apareceu
        letra = i

print(letra, quantidade)
