nomeArquivo = input('digite o nome do arquivo que você deseja abrir:' )
produto = []
valor = []
executar = True
Rodar = ''
nomeProduto = ''
valorProduto = 0
with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeArquivo}.txt','a+') as arquivoEntrada:
    while executar == True:
        rodar = input('digite S para continuar a adicionar produtos e N para encerrar a sua compra: ')
        if rodar.upper() == 'S':
            nomeProduto = input('digite o nome do produto: ')
            
            valorProduto = input('digite o valor do produto: ')
            if valorProduto.replace('.','', 1).isdigit():
                valorProduto = float(valorProduto)
                produto.append(nomeProduto)
                valor.append(valorProduto)

            else:
                print('digite um valor válido!')
        elif rodar.upper() == 'N':
            executar = False
        else:
            print('digite uma opção válida')
    
    print('\n')

    for i in range(0,len(produto)):
        arquivoEntrada.write(f'{produto[i]} : {valor[i]} \n')
    
    arquivoEntrada.write('\n')
    
    arquivoEntrada.write('-='*45)
    
    arquivoEntrada.write(f'\nO valor total é {sum(valor)}')
