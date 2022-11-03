arquivoEntrada = input('digite o nome do arquivo que você deseja criar: ')
executar = True
nome = ''
numero = ''

with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{arquivoEntrada}.txt','a+') as arquivo:
    while executar == True:

        
        nome = input('digite o seu nome: ')
        arquivo.write(nome + '\n')
        numero = input('Digite aqui o seu numero: ')
        if numero != '0':
            
            arquivo.write(numero + '\n')

        
        else:
            executar = False

