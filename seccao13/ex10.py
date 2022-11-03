vetor = []
ret = ''
c = 0
maiorNum = 0
maior = []
num = 0
nomeCidade = ''
habitantes = 0
executar = True
continuar = ''
nomeEntrada = input('digite o nome do arquivo de entrada: ')
nomeSaida = input('digite o nome do arquivo de saída: ')

#criando arquivo .txt de entrada de dados e adicionando nomes das cidades, e habitantes
with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeEntrada}','a+') as arquivoEntrada:
    while executar == True:
        continuar  = input('\nDigite S para adicionar mais uma cidade, ou N para encerrar o programa: ')
        if continuar.upper() == 'S':
            executar = True
            while c < 2:
                if c == 0:
                    nomeCidade = input('\ndigite o nome da cidade: ')
                    nomeCidade = nomeCidade + ',' 
                    c+= 1
                elif c ==1:
                    habitantes = input('digite o numero de habitantes: ')
                    if habitantes.isdigit():
                        habitantes = habitantes
                        

                        vetor.append(nomeCidade)
                        
                        vetor.append(habitantes)

                        vetor.append(' ')

                        for l in range(0,2):
                            if l == 0:
                                arquivoEntrada.writelines(vetor[l])
                            if l == 1:
                                arquivoEntrada.writelines(vetor[l] + ' \n ')
                            
                        
                        # arquivoEntrada.write('\n')

                        vetor.clear()

                        c+=1
                    else:
                        c = c 
                        print('digite um numero válido')
            c = 0
        
        else:
            Executar = False
            break
    
    arquivoEntrada.seek(0)
    ret = arquivoEntrada.read()
    print(arquivoEntrada.read())

    ret = ret.split(' ')


    for l in range(0, len(ret)):
        if ',' in ret[l]:
            num = ret[l].split(',')
            if int(num[1]) > maiorNum:
                maiorNum = int(num[1])
                maior = num

#criando arquivo de saida e adicionando o nome e a quantidade de habitantes da cidade mais populosa
with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeSaida}.txt','a') as arquivoSaida:
        
        arquivoSaida.write(f'Nome da cidade mais populosa: {maior[0]}\n Quantidade de pessoas: {maior[1]}')

        

    


