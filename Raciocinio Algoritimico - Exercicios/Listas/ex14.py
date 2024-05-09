'''14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente"'''

pergunta = ["Telefonou para a vítima? ('s/n')", "Esteve no local do crime? ('s/n')", "Mora perto da vítima? ('s/n')",
             "Devia para a vítima? ('s/n')", "Já trabalhou com a vítima?('s/n') "]
resposta = []
for perguntas in pergunta:
    respostas = input(perguntas)
    resposta.append(respostas)
    counter_yes = 0
for i in resposta:
    if i == 's':
        counter_yes += 1
if counter_yes == 2:
    print("Classificação: Suspeito")
elif counter_yes >= 3 and counter_yes <= 4:
    print("Classificação: Cúmplice")
elif counter_yes == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")