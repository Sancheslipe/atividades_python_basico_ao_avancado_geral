

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
print('-----------' * 4 ,'\n')
print('Matriz: ')



for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = (linha + 1) * (coluna + 1)

for i in matriz:
    print(i)


