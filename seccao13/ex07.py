paginasTotais = 0
palavraNova = 0 
EscreverNovaPagina = []
with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex01.txt')as arquivo1:
    paginasTotais = arquivo1.readlines() 
    for l in range(len(paginasTotais)):
        palavra = paginasTotais[l]
        
            
        print(palavra)
        palavra = palavra.replace('a','*')
                
            
        palavra = palavra.replace('e','*')

    
        palavra = palavra.replace('i','*')

    
        palavra = palavra.replace('o','*')

        palavra = palavra.replace('u','*')
            
        EscreverNovaPagina.append(palavra)

        print(palavra)
        
        print(EscreverNovaPagina)







with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex07.txt', 'a') as arquivo:
    
    for l in range(0,len(EscreverNovaPagina)):
        palavra = EscreverNovaPagina[l]
        arquivo.write(palavra)

    
    