vetor = []
num = 0
cont = 1

while cont <=5:
    num = input('digite um numero')
    if num.isdigit():
        num = int(num)
        vetor.append(num)
        cont +=1
    else:
        cont = cont
        print('digite um numero válido')
for i in range(0,4):
    if vetor[i] == 0:
        vetor.pop(i)

print(vetor)