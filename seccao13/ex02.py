import sys
nomeArquivo = input('digite o nome do arquivo que você deseja ver a quantidad de linhas: ')

try:
        with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\{nomeArquivo}.txt','r') as arquivo:
            linhas = arquivo.readlines()
            print(len(linhas))

except FileNotFoundError as e:
    print(f' o erro é {e}')
        
    print(f'\n Digite um nome de arquivo existente! \n')

    
