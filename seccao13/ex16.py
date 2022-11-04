vetor = []
vetorBin = []
num = 0 
l = 0


while l<10:
    
    num = input(f'{l}digite um numero: ')
    if num.isdigit():
        num = int(num)
        vetor.append(num)
        vetorBin.append(bin(num)[2:])     
            
        l += 1

    else:
        l = l
        print('digite um numero válido!')


nomeArquivo = input('Digite o nome do arquivo que você deseja criar: ')

with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeArquivo}.txt','x') as arquivo:

    for l in range(0,len(vetorBin)):
        arquivo.write(vetorBin[l] +'\n')

    print('the program has ended')
