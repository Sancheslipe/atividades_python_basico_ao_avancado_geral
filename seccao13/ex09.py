textoTotal1 = 0
textoTotal2 = 0
textoTotal3 = []
with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex07.txt') as arquivo1:
    textoTotal1 = arquivo1.readlines()

with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex08.txt') as arquivo2:
    textoTotal2 = arquivo2.readlines()

textoTotal3.append(textoTotal1)
textoTotal3.append('\n')
textoTotal3.append(textoTotal2)
with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex09.txt','a') as arquivo3:
    for l in range(0,len(textoTotal3)):
        for i in range(0,len(textoTotal3[l])):
            linha = textoTotal3[l][i]
            arquivo3.write(linha)