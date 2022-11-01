matriz = [[],[],[]]
coluna = []
transposta = [[],[],[],[]]
inversa = [[],[],[],[]]

calc = 0
num = 0

for l in range(0,3):
    for c in range(0,4):
        num = input('digite um numero')
        if num.isdigit():
            coluna.append(int(num))
            matriz[l].append(coluna[:])
            coluna.clear()
        else:
            print('digite um numero válido')
print(matriz)

for l in range(0,3):
    for c in range(0,4):
        transposta[c].append(matriz[l][c])
        
inversa = transposta[::-1]


for l in range(0,3):
    for c in range(0,4):
        print(f'{matriz[l][c]}', end= ' ')
    print()

print('\n')

for l in range(0,4):#4
    for c in range(0,3):
        print(f'{transposta[l][c]}', end = ' ')
    print()
print('\ninversa\n')
print('-='*35)

for l in range(0,4):
    for c in range(0,3):
        print(f'{inversa[l][c]}', end= ' ')
    print()

print('\n')

