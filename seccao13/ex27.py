class Aluno:
    def __init__(self,nome,nota,aprovado) :
        self.nome = nome
        self.nota = nota
        self.aprovado = aprovado

        pass

executar = True
vetor = []
qtde = 0
mediaGeral = 0
notas = 0
notaAluno = []

while executar == True:
    print('\n(a) Definir informações da turma \n(b) Inserir aluno e nota\n(c) exibir alunos e médias')
    print('(d) exibir alunos aprovador\n(e) exibir alunos reprovados\n(f) salvar dados em disco\n(g) Sair do programa (fim)\n')

    opcao = input('digite aqui a sua opção: ')

    if opcao.lower() == 'a':
        qtde = input('digite quantos alunos você tem: ')
        if qtde.isdigit():
            qtde = int(qtde)

            mediaGeral = input('digite a média da turma: ')
            if mediaGeral.isdigit():
                mediaGeral = int(mediaGeral)
                notas = input('digite quantas notas o aluno possui: ')
                if notas.isdigit():
                    notas = int(notas)
                else:
                    print('digite um numero válido!')
            else:
                print('digite um numero válido!')

        else:
            print('digite um numero válido!')


    elif opcao.lower() == 'b':
        for l in range(0, int(qtde)):
            nome = input('\n digite o nome do aluno: ')
            
            for c in range(0,int(notas)):
                nota = input(f' digite a nota {c+1} de {nome}: ')
                
                if nota.replace('.',' ', 1).replace('-','').isdigit():
                    nota = float(nota)

                
                else:
                    nota = 'error'
                notaAluno.append(nota)
            
            if sum(notaAluno)/float(notas) >= float(mediaGeral):
                sit = True
            else:
                sit = False
            
            aluno = Aluno(nome,notaAluno[:],sit)

            vetor.append(aluno)
         
            notaAluno.clear()


    elif opcao.lower() == 'c':
        for l in range(0,int(qtde)):

            media = sum(vetor[l].nota) / int(notas)
            print(f' aluno:{str(vetor[l].nome).title()} media:{media}', end = '\n')


    elif opcao.lower() == 'd':
        for l in range(0,int(qtde)):
            if vetor[l].aprovado == True:
                print(f'aluno:{vetor[l].nome} aprovado! ', end = '\n')


    elif opcao.lower() == 'e':
        for l in range(0,int(qtde)):
            if vetor[l].aprovado != True:
                print(f'aluno:{vetor[l].nome} reprovado! ', end = '\n')

    elif opcao.lower() == 'f':
        with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\ex27.txt','a') as arquivo:
            for l in range(0,int(qtde)):
                arquivo.write(f'nome:{vetor[l].nome}\n')
                
                arquivo.write(f'notas:{vetor[l].nota}\n')
                
                if vetor[l].aprovado == True:
                    arquivo.write(f'situação: Aprovado \n')
                else:
                    arquivo.write(f'situação: Reprovado \n')



    
    elif opcao.lower() == 'g':
        executar = False

print(f'fim')