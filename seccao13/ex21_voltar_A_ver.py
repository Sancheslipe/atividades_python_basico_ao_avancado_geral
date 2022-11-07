import pickle
compNome = 40
vetorNome = []
vetorNota = []
contx = 0
conty = 0
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

with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\Disciplina.txt','a') as Disciplina:
    for l in range(0,len(vetorNota)):
        Disciplina.write(f'{vetorNome[l]}: {vetorNota[l]}' + '\n')

with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\ex21.txt', 'w') as arquivo:
    for l in range(0,len(vetorNota)):
        arquivo.write(f'{vetorNome[l]}: {vetorNota[l]}')
        # pickle.dumps('hello', arquivo)
