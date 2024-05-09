pessoas = {}
while True:
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo M/F: ')
    idade = int(input('Digite sua idade: '))
    pessoas[nome] = {'Idade': [idade], 'Sexo': sexo}

