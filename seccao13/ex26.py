class Aluno:
    def __init__(self,matricula,sobrenome,anoNascimento) :
        self.matricula = matricula
        self.sobrenome = sobrenome
        self.anoNascimento = anoNascimento

        pass


aluno =[]


qtde = input('digite o numero de alunos que será armazenado: ')
if qtde.isdigit():
    qtde = int(qtde)
    for l in range(0,qtde):
        matri = input('\ndigite aqui a sua matricula: ')
        sobre = input('digite o seu sobrenome (apenas1) : ')
        ano_de_nascimento = input('digite o seu ano de nascimento: ')

        inf = Aluno(matri,sobre,ano_de_nascimento)
        aluno.append(inf)




else:
    print('digite um numero válido!')


with open (f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\alunos.txt','a') as arquivo:
    for l in range(0, len(aluno)):
        for c in range(0,3):
            if c == 0:
                arquivo.write('\n'+aluno[l].matricula + '\n')
                
            elif c == 1:
                arquivo.write(aluno[l].sobrenome + '\n')
            elif c == 2:
                arquivo.write(aluno[l].anoNascimento + '\n')
                arquivo.write('-='*45)
    

print('arquivo finalizado')

