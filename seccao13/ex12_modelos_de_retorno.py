alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
caracTotais =''
linhasTotais = 0



#abrindo u arquivo aleatório e printando na tela quantas vezes cada letra ocorre.
with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\cafe.txt') as arquivo:
    caracTotais = arquivo.read()
    palavras = caracTotais.split( )
    linhasTotais = caracTotais.split('\n')

    print(f'O total de palavras é: {len(palavras)}\n')
    print(f'O  total de linhas é: {len(linhasTotais)}\n')
    print(f'O total de caracteres é: {len(caracTotais)}\n')
    print('O total de cada letra é:')
    print('\n' * 2)       
    for l in range(0,26):
        print(f'{alfabeto[l]}: {caracTotais.count(alfabeto[l])}', end =' ')
        if l % 5 == 0:
            print('\n')