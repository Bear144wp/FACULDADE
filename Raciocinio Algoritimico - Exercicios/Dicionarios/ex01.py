estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}
print(f'Estoque atual: {estoque}')
print(f'Abaixo segue o cardápio:')
print('-'*20)
for items, ingredientes in cardapio.items():
    print(items)
print('-'*20)
while True:
    inputz = input('O que deseja pedir? ("0" para sair): ')
    if inputz == '0':
        print('Finalizado! ')
        break
    elif inputz not in cardapio.keys():
        print('Não está no cardápio, tente novamente!')
        continue
    ingredientes = cardapio[inputz]
    condicao = False
    ingredientes_faltantes = []
    for ingrediente in ingredientes:
        if ingrediente not in estoque or estoque[ingrediente] == 0:
            print('Não temos os ingredientes necessários!')
            ingredientes_faltantes.append(ingrediente)
            print(f'Ingredientes faltantes: {ingredientes_faltantes} qntd disponivel: {estoque[ingrediente]}')
            condicao = True
    if not condicao:
        print('Saindo seu pedido!')
        for ingrediente in ingredientes:
            estoque[ingrediente] -= 1
print(f'ESTOQUE ATUAL: {estoque}')




            



'''- Se não tiver os ingredientes para o preparo do produto em estoque mostrar uma
mensagem para cada ingrediente faltante “Infelizmente acabou o {ingrediente}”'''