vetor = [[],[],[],[],[]]
l = 0
c = 0
nomeCidade = ''
habitantes = 0
palavra = 0

with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\Cidade_mais_ppulosa.txt') as arquivoEntrada:
    while l < 5:
        while c < 2:
            if c == 0:
                nomeCidade = input(' digite o nome da cidade: ')
            elif c ==1:
                habitantes = input('digite o numero de habitantes: ')
                if habitantes.isdigit():
                    habitantes = int(habitantes)

                    vetor[l].append(nomeCidade)
                    vetor[l].append(habitantes)
                
                else:
                    c = c 
                    print('digite um numero válido')

    for l in range(0,len(vetor)):
        for c in range(0,len(vetor[l])):
            if c == 0:
                palavra = vetor[l][c]
            elif c == 1:
                habitante = vetor[l][c]
            
            arquivoEntrada.write(palavra)
            arquivoEntrada.write(habitante)
