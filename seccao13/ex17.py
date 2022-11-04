matrizA = [] 
line = 0
col = 0
quantAnul = 0
anul = []
linhaAnulada = 0
colunaAnulada = 0
cont = 0

nomeArquivoEntrada = input('digite aqui o nome do arquivo que você deseja colocar as informações: ')
with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeArquivoEntrada}.txt','a+') as arquivo1:

    linha = input('digite um numero inteiro numero referente á quantidade de linhas da matriz: ')
    if linha.isdigit(): 
        linha = int(linha)
        coluna = input('digite um numer inteiro referente á quantidade de colunas da matriz: ') 
        
        if coluna.isdigit():
            coluna = int(coluna)
            quantAnul = input('digite quantos numero você deseja anular:')
            
            if quantAnul.isdigit() and int(quantAnul) < (linha * coluna):
                quantAnul = int(quantAnul)
                arquivo1.write(f'{linha}{coluna}{quantAnul} \n')
                
                while cont < quantAnul:
                    
                    linhaAnulada = input('digite a linha o numero que deseja apagar: ')
                    
                    if len(linhaAnulada) == 1 and linhaAnulada.isdigit():
                        linhaAnulada = int(linhaAnulada)  
                        colunaAnulada = input('digite a coluna o numero que deseja apagar: ')

                        if len(colunaAnulada) == 1 and colunaAnulada.isdigit():
                            colunaAnulada = int(colunaAnulada)
                            arquivo1.write(f'{linhaAnulada}{colunaAnulada}' + '\n')
                            cont +=1
                        else:
                            cont = cont
                            print('digite uma linha válida')
                    else:
                        cont = cont
                        print('digite uma linha válida')

                    print('\n')



            else:
                print('digite um numero válido, menor ou igual a quantidade de posições!')

        else:
            print('digite  um numero válido')
        
    else:
        print('digite um numero válido')






with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeArquivoEntrada}.txt','r') as arquivoEntrada:
    test = arquivoEntrada.readline()
    

    linha = int(test[0])
    coluna = int(test[1])
    quantAnul = int(test[2])

    for l in range(0,linha):
        matrizA.append([])

    
    for l in range(0,linha):
        for c in range(0,coluna):
            matrizA[l].append(1)
    
    for i in range(0,quantAnul):
        posiAnul = arquivoEntrada.readline()
        linhaAnulada = int(posiAnul[0])
        colunaAnulada = int(posiAnul[1])

        anul.append(posiAnul[0:2])
        matrizA[linhaAnulada][colunaAnulada] = 0 
    
    

nomeSaida = input('\nDigite o nome do arquivo de saída: ')

with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeSaida}.txt','a') as arquivoSaida:

    for l in range(0,linha):
        for c in range(0,coluna):
            arquivoSaida.write(f'[{matrizA[l][c]}] ' )
        arquivoSaida.write('\n')

