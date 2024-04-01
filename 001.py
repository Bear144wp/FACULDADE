''' exercicio 1
numeroP = 0
numeroI = 0
for i in range(1,6):
    numeros = int(input('Digite o ' + str(i) + ' numero: '))
    if numeros % 2 == 0:
        numeroP += 1
    elif numeros % 2 != 0:
        numeroI += 1
print(f'O total de números par é {numeroP}, e números impar: {numeroI}')'''

#exercicio 2
'''num_menor = 0
num_maior = 0
for i in range(1,6):
    num = int(input('Digite o {} num: '.format(i)))
    if i == 1:
        num_menor = i
        num_maior = i
    else:
        if num > i:
            num_maior = num
        if num < num_menor:
            num_menor = num
print(f'O maior é {num_maior} e o menor {num_menor}')'''

#exercicio 3
'''texto = input('Digite o texto pra remover as vogais: ')
vogal = 'aeiou'
texto_sem_vogal = ''
for letra in texto:
    if letra not in vogal:
        texto_sem_vogal += letra
print(texto_sem_vogal)'''

#exercicio 8

'''Criar um programa que gera a série de Fibonacci até enquanto o
valor for menor que um valor informado pelo usuário. Obs.: Série de
Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55,... é formada por 0, 1 e
partir deste ponto sempre será a soma dos dois valores anteriores.
'''
'''valor_user = int(input('Digite um valor para limite: '))
fibonacci_atual = 0
fibonacci_proximo = 1
while fibonacci_atual <= valor_user:
    print(fibonacci_atual)
    fibonacci_atual, fibonacci_proximo = fibonacci_proximo, fibonacci_atual + fibonacci_proximo


'''

#exercicio 6

'''Criar um programa que pede para o usuário inserir um login e uma
senha. Caso os valores sejam iguais, informar que os dados são
inválidos e pedir novamente as informações. Caso contrário, exibir a
mensagem "Bem-vindo ao sistema!!!".'''

'''while True:
    login = input('Digite seu login')
    senha = input('Digite sua senha')
    if login == senha:
        print('Seus dados não podem ser iguais')
        continue
    else:
        break'''

#exercicio 7

'''Criar um programa que solicite ao usuário vários números e, ao
digitar 0, calcula a média destes números informados.'''

'''contador = 0
soma_valor = 0
while True:
    valores = int(input('Digite os valores: '))
    contador += 1
    soma_valor += valores
    if valores == 0:
        divisao = soma_valor / contador
        print(divisao)'''

'''exercicio 9
Criar um programa que simula um carrinho de compras, onde
solicita o nome do produto (não pode ser vazio), o valor deste
produto (valor com vírgula, positivo) e a quantidade deste
produto a ser comprada (valor inteiro, positivo). Ao incluir um
produto, deve perguntar se o usuário deseja fechar o pedido ou
incluir mais produtos. Todos os dados devem ser validados. Ao
final da compra, deve ser informado o valor total do pedido.

carrinho = []
while True:
    opcoes = int(input('Digite:\n1 - Incluir Produto\n2 - Fechar pedido'))
    if opcoes == 1:
        print('Ótimo, para adicionar um novo produto, siga as opções abaixo: ')
        nome_p = input('Qual o nome do produto? ')
        valor_p = float(input('Valor do produto: '))
        quantidade_p = int(input('Quantidade do produto: '))
        carrinho.append((valor_p, quantidade_p))
    elif opcoes == 2:
        valor_total = sum(valor * quantidade for valor, quantidade in carrinho) 
        print(f'Vamos fechar seu pedido!\nO valor total do pedido foi de: R$ {valor_total}')
        break'''


'''exercicio 10 
Criar um Programa que simule um caixa eletrônico. O programa
deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. A saber:
a. Notas disponíveis: 1, 5, 10, 50 e 100 reais;
b. Valor mínimo de saque: R$ 10,00 reais;
c. Valor máximo de saque: R$ 600,00 reais.
Este é o mesmo exercícios de desafio de condicionais. Porém,
agora o desafio é resolver de forma mais otimizada fazendo uso
de estruturas de repetição'''

valor_min = 10
valor_max = 600
valor = int(input('Quanto deseja sacar? R$'))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
