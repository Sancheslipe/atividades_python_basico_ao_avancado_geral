compNome = 40
vetorNome = []
vetorNota = []
contx = 0
conty = 0
maiorNum = 0.0 
maior = ''
quantidade = input('digite quantos alunos você possui')
if quantidade.isdigit():
    quantidade= int(quantidade)


    while contx < quantidade:
        nome = input('digite seu nome: ')
        
        if len(nome) == 40:
            vetorNome.append(nome)   
        elif len(nome) < 40:
            nome += ' ' * (compNome - len(nome))
            nome = nome 
            vetorNome.append(str(nome))
        
        if conty <= 1:
            nota = input('digite aqui a sua nota: ')
            if nota.replace('.','', 1).replace('-','').isdigit():
                nota = float(nota)
                vetorNota.append(str(nota))
                conty += 1
            else:
                conty = conty
                print('digite uma nota válida: ')

            
        else:
            contx = contx
            print('digite um nome com 40 caracteres!')
        
        
        contx +=1
        conty = 0

else:
        print('digite um numero válido')

with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\ex21_entrada.txt','w') as Disciplina:
    
    for l in range(0,len(vetorNota)):
        Disciplina.write(f'{vetorNome[l]}: {vetorNota[l]}' + '\n')

    

with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\ex21_entrada.txt', 'r') as lerArquivo:
    lerArquivo.seek(0)
    ler = lerArquivo.read()

    array = ler.split('\n')
    # print(f'a len de array é:{len(array)}')
    for l in range(0,(len(array))-1):
        # print(array[l])
        if float(array[l][41::]) > float(maiorNum):
            maiorNum = float(array[l][41::])
            maior = array[l][0:40]

with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\ex21.txt','w') as arquivoFinal:
    arquivoFinal.write(f' o aluno com a maior nota é:{maior}\n e a sua nota foi:{maiorNum}')