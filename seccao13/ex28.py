arquivodeEntrada = input('digite o nome do arquivo de entrada: ')
#ex28
ler = ''

with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\{arquivodeEntrada}.txt','r') as arquivoEntrada:
    ler = arquivoEntrada.read()
    linhasTotais = ler.split('\n')
   
    
arquivoDeSaida = input('digite aqui o nom e do arquivo de saida: ')
#ex28S
with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\{arquivoDeSaida}.txt','w') as arquivoSaida:
    for l in range((len(linhasTotais)-1), -1,-1 ):
        palavra = linhasTotais[l]
        for c in range((len(linhasTotais[l])-1),-1,-1):
            arquivoSaida.write(palavra[c])
        arquivoSaida.write('\n')