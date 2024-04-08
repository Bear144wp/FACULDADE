'''1. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
final e o tempo calculado em segundos'''

massa = 10.0
segundos = 0

while massa >= 0.5:
    massa /= 2
    segundos += 50

print(f'Massa final: {massa}, Segundos decorridos: {segundos}')