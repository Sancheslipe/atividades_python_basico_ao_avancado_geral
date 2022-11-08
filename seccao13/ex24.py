executar = True
opcao = ''
escrever = []
relatorioGeral = []    #split('\n') de vezes len(tudo)
produtosIndisponiveis = []
cod = ''
desc = ''
qtde = 0.0

while executar == True:
    print('Digite [A] para adicionar um produto|\nDigite [X] para fazer ma retirada|')
    print('Digite [R] Para obter o relatório Geral|\nDigite [N] para obter o relatório de itens não disponíveis|\n')
    opcao = input('Digite aqui a sua opcção: ') 

    if opcao.upper() == 'A':
        cod = input('digite aqui o código do produto: ')
        desc = input('digite aqui a descrição do produto: ')
        qtde = input('digite aqui a quantidade do produto: ')
        if (qtde.replace('.','', 1).isdigit()) and float(qtde) > 0:
            qtde = float(qtde)
            escrever.append(f'cod:{cod}\n')
            escrever.append(f'desc:{desc}\n')
            escrever.append(f'quantidade:{qtde}\n')
            escrever.append('-='* 35 + '\n')
            with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\dipensa.txt','a+') as arquivoA:
                for l in range(0,4):
                    arquivoA.write(escrever[l])

            executar = False
        else:
            print('digite uma quantidade válida!')
            executar = False

    elif opcao.upper() == 'X':
        retirada = input('digite nome do produto que deseja fazer a retirada: ')
        with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\dipensa.txt','r+') as arquivoB:
            ler = arquivoB.read()
            ler = ler.split('\n')
            
            for l in range(0,len(ler)-1):
                
                if ler[l][0:4] == 'desc':
                    
                    if retirada in ler[l][5::]:
                        total = float(ler[l+1][11::])
                        print(f'total disponivel para retirada: {total}')
                        qtdeRetirada = input(f'Digite o valor que deseja retirar :')

                        if (qtdeRetirada.replace('.','', 1).isdigit()) and (float(qtdeRetirada) <= float(total)):

                            result = str(float(total) - float(qtdeRetirada) )
                            print(f' o result é : {result}')
                            ler[l + 1] = ler[l + 1][0:11] + result
                            print(ler[l + 1])
                        
                        else:
                            print('digite uma quantidade válida para retirada!')
                            executar = False
                    else:
                        print('digite um produto válido para retirar')
                        executar = False

        with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\dipensa.txt','a+') as Escrever:
            for l in range(0,len(ler)):
                arquivoB.write(ler[l] + '\n')





    elif opcao.upper() == 'R':
        print('')
    elif opcao.upper() == 'N':
        print('')
    else:
        print('digite uma opção válida!')