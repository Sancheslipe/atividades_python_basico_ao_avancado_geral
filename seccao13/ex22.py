compNome = 40
cont = 0
arquivoEntrada = input('digite o nome do arquivo de entrada: ')
nome = input('digite seu nome: ')
nota = 0
notas = []
ler = 0

while cont < 1:    
    if len(nome) == 40:
        nome = nome   
    elif len(nome) < 40:
            nome += ' ' * (compNome - len(nome))
    else:
        print('digite um nome válido')
    cont += 1

cont = 0

while cont < 3:
    nota = input('digite aqui a sua nota: ')
    if nota.replace('.','', 1).replace('-','').isdigit():
        nota = float(nota)
    
        notas.append(nota)
        cont+=1
    
    else:
        cont = cont
        print('digite uma nota válida')


with open(f'C:\\Curso01_github\\seccao13\\arquivos_de_texto\\{arquivoEntrada}.txt','a+') as arquivo:
    arquivo.write(nome + '\n')
    for l in range(0,len(notas)):
        arquivo.write(f'{str(notas[l])} ')

    arquivo.seek(0)
    ler = arquivo.read()
    notas.clear()

arquivoSaida = input('digite aqui o nome do arquivo de saida: ')
with open(f'C:\\Curso01_github\\seccao13\\arquivos_de_texto\\{arquivoSaida}.txt','a+') as arquivoSaida:
    ler = ler.split()
    arquivoSaida.write(ler[0] + '\n')
    for l in range(1,4):
        notas.append(ler[l])
    
    notas.sort()
    for l in range(0,len(notas)):
        arquivoSaida.write(str(notas[l]) + ' ')

