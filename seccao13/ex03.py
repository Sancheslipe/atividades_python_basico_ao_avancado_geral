with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex01.txt')as arquivo:
    paginasTotais = arquivo.readlines()
    vogais = 0 
    for l in range(len(paginasTotais)):
        palavra = paginasTotais[l]
        for i in range(len(palavra)): 
            
            if 'a' == palavra[i]:
                vogais += 1
            elif 'e' == palavra[i]:
                vogais += 1
            elif 'i' == palavra[i]:
                vogais += 1
            elif 'o' == palavra[i]:
                vogais += 1
            elif 'u' == palavra[i]:
                vogais += 1
            
    print(f'a quantidade de vogais é {vogais}')
    