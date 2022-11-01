paginasTotais = 0
with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex07.txt')as arquivo1:
    paginasTotais = arquivo1.readlines() 
    

  

with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex08.txt', 'a') as arquivo2:
    
    for l in range(0,len(paginasTotais)):
        palavra = paginasTotais[l]
        arquivo2.write(palavra.upper())

    
    