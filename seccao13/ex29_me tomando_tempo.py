nomeArquivo = input('digite aqui o nome que você deseja dar ao arquivo: ')

codigo_vendedor = 0
valor_da_venda = 0
mes = 0
ler = 0

with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\{nomeArquivo}', 'a+') as arquivoEntrada:
    

    codigo_vendedor = input('digite aqui o seu codigo de vendedor: ')

    nome_vendedor = input('digite aqui o nome do vendedor: ')
    
    valor_da_venda = input('digite aqui o valor da venda: ')
    
    mes = input('digite aqui o mes: ')
    
    if int(mes) <= 12 and int(mes) >= 1 and mes.isdigit():
        mes = int(mes)
        
        arquivoEntrada.write('Código do Vendedor: ' + codigo_vendedor + '\n')
        arquivoEntrada.write('Nome do Vendedor: ' + nome_vendedor + '\n')
        arquivoEntrada.write('valor: ' + valor_da_venda + '\n')
        arquivoEntrada.write('mes: ' + str(mes) + '\n')
        arquivoEntrada.write('-='*35 + '\n')

    else:
        print('digite um mes válido!')

    arquivoEntrada.seek(0)
    ler = arquivoEntrada.read()
    linha = ler.split('\n')


ask = input('deseja excluir algum vendedor do arquivo? S,N')
    

if ask.upper() == 'S':
    excluir_nome = input('digite aqui o nome que você deseja excluir! ')
        
    for l in range(0,len(linha)):
        if excluir_nome in linha[l]:
            print('passou aqui!!!!!')
            print(ler.index(excluir_nome))
            test = ler.index(excluir_nome)
            with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\test','w') as escreverArquivo:
                escreverArquivo.seek(0)
                escreverArquivo.write('excluído')
                
            # if excluir_nome in linha[l][18::]:
                
            #     linha[l][18:::] = 'vendedor Excluido'   

