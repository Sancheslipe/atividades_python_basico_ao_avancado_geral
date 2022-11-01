matriz = [[],[],[],[]]
coluna = 0
for l in range(0, 4):
    for c in range(0, 4):
        if l == 0:

            coluna = int(input(f'digite um numero referente á {l},{c}: '))
            matriz[l].append(coluna)
        elif c == 0:
            coluna = int(input(f'digite um numero referente á {l},{c}: '))
            matriz[l].append(coluna)
        else:
            coluna = '00'
            matriz[l].append(coluna)

for l in range(0,4):
    for c in range(0,4):
        if matriz[l][c] == '00':
              
            coluna = matriz[l-1][c] * matriz[l][c -1]
            matriz[l][c] = coluna
        
            
for l in range(0, 4):
    for c in range(0, 4):
        print(f'{matriz[l][c]}', end='       ')

    print()

