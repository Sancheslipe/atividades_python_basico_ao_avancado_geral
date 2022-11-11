with open(f'C:\\Curso01_github\\seccao13\\arquivos_de_texto\\ex19.txt') as arquivo:
    teste = arquivo.read()
    teste = teste.split('\n')
    nomeMaior = 0
    maior = 0 
    num = 0
    for l in range(len(teste)-1):

        dados = teste[l].split()
        num = dados[3]
        nome = dados[1]
        num = float(num)
        if num > maior:
            maior = num
            nomeMaior = nome
    
    print(f'\na maior nota foi {maior} e ela pertence á {nomeMaior}')