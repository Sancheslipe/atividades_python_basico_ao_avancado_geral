with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\ex19.txt') as arquivo:
    teste = arquivo.read()
    teste = teste.split()
    nomeMaior = 0
    maior = 0 
    num = 0
    for l in range(len(teste)):
        
        if l % 2 != 0:
            num = float(teste[l][5::])
            if num > maior:
                maior = num
                nomeMaior = teste[l-1][5::]
    
    print(f'\na maior nota foi {maior} e ela pertence á {nomeMaior}')