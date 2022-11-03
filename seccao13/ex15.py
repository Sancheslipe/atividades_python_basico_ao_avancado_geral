executar = True
rodar = ''
nome = 0 
dia = 0
mes = 0 
ano = 0
dataNascimento = 0
lerArquivo1 = 0
linhasTotais = 0
idade = []
calculo = 0
mensagem = ''





anoCorrente = input('Digite o ano corrente: ')

if anoCorrente.isdigit():
    anoCorrente = int(anoCorrente)
else:
    print('digite um ano válido')

nomeEntrada = input('Digite o nome do arquivo que você deseja criar: ')

nomeSaida = input('digite o nome do arquivo que você deseja criar para a saida: ')

with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeEntrada}.txt','a+') as arquivoEntrada:
    
    while executar == True: 
        rodar = input('se deseja adicionar mais um iten digite S, caso deseja encerrar o programa digite N: ')
        if rodar.upper() == 'S':
            nome = input('digite aqui o seu nome: ')

            dia = input('digite o dia de se nascimento: ')
            if dia.isdigit() and int(dia) <= 31 and int(dia) > 0:
                dia = int(dia)

                mes = input('digite aqui o mes do seu nascimento: ')
                if mes.isdigit() and int(mes) >=1 and int(mes)<=12:
                    mes = int(mes)
                    ano = input('digite aqui o ano de seu nascimento: ')
                    if ano.isdigit():

                        ano = int(ano) 

                        dataNascimento = f'{str(dia)}/{str(mes)}/{str(ano)}'
        
                        arquivoEntrada.write(nome+' ')
                        arquivoEntrada.write(dataNascimento+ '\n')
                        calculo = int(anoCorrente) - int(ano)
                        if dia == 3 and mes == 11:
                            #variavel calculo criada pois o vs code não deixou eu colocar ano corrente - ano
                            print(f'ano corrente {anoCorrente}')
                            print(f'ano {ano}')
                            
                            # ta tudo em int pois estava dando uma corrente vermelha de erro dizendo que não era possivel fazer uma operação com string and int
                            idade.append(calculo +1)
                            break
                        else:
                            idade.append(calculo)

                    else:
                        print('digite um ano válido ')
                else:
                    print('digite um mes válido')
            else:
                print('digite um dia válido')
            
        elif rodar.upper() == 'N':
            executar = False
        else:
            print('digite uma letra válida')
    
    arquivoEntrada.seek(0)
    lerArquivo1 = arquivoEntrada.read()


with open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\{nomeSaida}.txt','a+') as arquivoSaida:
    linhasTotais = lerArquivo1.split('\n')

    for l in range(0, len(linhasTotais)-1):
        # divide os nomes das datas
        nomes = linhasTotais[l].split()
        arquivoSaida.write(nomes[0] + ' ')
        
        print(f'\n{idade[l]}\n')

        if idade[l] <18:
            mensagem = 'menor de idade'
        elif idade[l] == 18:
            mensagem = 'entrando na maior idade'
        elif idade[l] > 18:
            mensagem = 'maior de idade'
        arquivoSaida.write(mensagem + '\n')
        