cont1 = 0
cont2 = 0
profissoes = []
tempoDeServico = []
profissao =''
tempoServico = ''


while cont1 <5 :
    
    while cont2 < 1:
        profissao = input(' digite aqui a sua profissão: ')
        tempoServico = input('digie aqui o seu tempo de serviço em anos: ')
        if tempoServico.replace('.','', 1).isdigit():
            profissoes.append(profissao)
            tempoDeServico.append(tempoServico)
            cont2 +=1
        else:
            cont2 = cont2
            print('digite um tempo de serviço válido')

    cont1+=1
    cont2 = 0

with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\emp.txt','w') as arquivo:
    for l in range(0, cont1):
        arquivo.write(f'{profissoes[l]} : {tempoDeServico[l]} \n')
    
