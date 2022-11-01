with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex01.txt')as arquivo:
    paginasTotais = arquivo.readlines()
    vogais = 0 
    consoantes = 0
    for l in range(len(paginasTotais)):
        palavra = paginasTotais[l].lower()
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
            
            if 'b' == palavra[i]:
                consoantes += 1
            elif 'c' == palavra[i]:
                consoantes += 1
            elif 'd' == palavra[i]:
                consoantes += 1
            elif 'f' == palavra[i]:
                consoantes += 1
            elif 'g' == palavra[i]:
                consoantes += 1
            elif 'h' == palavra[i]:
                consoantes += 1
            elif 'j' == palavra[i]:
                consoantes += 1
            elif 'k' == palavra[i]:
                consoantes += 1
            elif 'l' == palavra[i]:
                consoantes += 1
            elif 'm' == palavra[i]:
                consoantes += 1
            elif 'n' == palavra[i]:
                consoantes += 1
            elif 'p' == palavra[i]:
                consoantes += 1
            elif 'q' == palavra[i]:
                consoantes += 1
            elif 'r' == palavra[i]:
                consoantes += 1
            elif 's' == palavra[i]:
                consoantes += 1
            elif 't' == palavra[i]:
                consoantes += 1
            elif 'x' == palavra[i]:
                consoantes += 1
            elif 'y' == palavra[i]:
                consoantes += 1
            elif 'z' == palavra[i]:
                consoantes += 1

    print(f'a quantidade de vogais é {vogais}')
    print(f'a quantidade de consoantes é {consoantes}')