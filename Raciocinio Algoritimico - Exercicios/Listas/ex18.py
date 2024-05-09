votos = []
while True:
    print('Enquete: Quem foi o melhor jogador?')
    inputz = int(input('Número do jogador (Para finalizar digite 0): '))
    if inputz == 0:
        break
    elif inputz not in range(1, 24):
        print('Digite números entre 1 e 23 apenas! ')
    else:
        votos.append(inputz)
print("Resultado da votação: ")
print(f"Foram computados {len(votos)}")