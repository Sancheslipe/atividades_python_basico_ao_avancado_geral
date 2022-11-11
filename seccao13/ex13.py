executar = True
nome = ''
numero = ''
nomeArquivo = input('digite aqui o nome do arquivo: ')
with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\{nomeArquivo}.txt','a+')as arquivo:
    while executar == True:

        
        nome = input('digite o seu nome: ')
        arquivo.write(nome + '\n')
        numero = input('Digite aqui o seu numero: ')
        if numero != '0':
            
            arquivo.write(numero + '\n')
            arquivo.write('\n'+'-='*20+'\n')

        
        else:
            executar = False

