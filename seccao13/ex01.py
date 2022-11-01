with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex01.txt', 'a') as arquivo:
    executar = True
    while executar == True:
        caractere = input('digite o caracter que quiser ou [0] para sair: ')
        if caractere != '0':
            arquivo.write(caractere + '\n')
        else:
            executar = False
    
    

