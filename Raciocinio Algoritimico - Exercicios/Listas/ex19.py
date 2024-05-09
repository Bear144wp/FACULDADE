
opcoes = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = []
for i, j in enumerate(opcoes):
    print('Avalie com nota de 1 a 10: ')
    inputzao = input(f'{i+1} - {j}')
    votos.append(inputzao)
