nomeEntrada = input('digite o nome de entrada do arquivo: ')
palavra = input('\ndigite aqui a palavra que você deseja procurar no arquivo: ')


with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeEntrada}.txt','a+') as arquivoEntrada:
    arquivoEntrada.seek(0)
    linhas = arquivoEntrada.read()
    linhas = linhas.split()
    
    print(linhas.count(palavra))

#teste com o arquivo café, e a palavrs café 