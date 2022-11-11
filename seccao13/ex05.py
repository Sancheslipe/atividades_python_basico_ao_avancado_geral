nomeArquivo = input('digite aqui o nome do arquivo: ')
try:
    with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\{nomeArquivo}.txt')as arquivo:
        caractere = input('digite o caractere que você deseja ver a quantidade de repetições: ')
        linhasTotais = arquivo.readlines()
        qtde = 0
        for l in range(len(linhasTotais)):
            linha = linhasTotais[l]
            for i in range(len(linha)):
                
                if caractere == linha[i]:
                    qtde +=1
        
        print(f' a quantidade que o caractere {caractere} ocorre no arquivo é {qtde}')
except Exception as e:
    print(f' o erro é {e}')
    print('digite um nome de arquivo válido')        