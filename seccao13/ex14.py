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






nomeEntrada = input('Digite o nome do arquivo que você deseja criar: ')

nomeSaida = input('digite o nome do arquivo que você deseja criar para a saida: ')
with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\{nomeEntrada}.txt','a+')as arquivoEntrada:
    
    while executar == True: 
        rodar = input('se deseja adicionar mais um iten digite S, caso deseja encerrar o programa digite N: ')
        if rodar.upper() == 'S':
            nome = input('digite aqui o seu nome: ')

            dia = input('digite o dia de se nascimento: ')
            if dia.isdigit() and int(dia) <= 31 and int(dia) > 0:
                dia = int(dia)

                mes = input('digite aqui o mes do seu nascimento: ')
                if mes.isdigit() and int(mes) >=1 and int(mes)<=12:

                    ano = input('digite aqui o ano de seu nascimento: ')
                    if ano.isdigit():
                        ano = int(ano)  
                        dataNascimento = f'{dia}/{mes}/{ano}'
                        arquivoEntrada.write(nome+' ')
                        arquivoEntrada.write(dataNascimento+ '\n')
                        
                        if dia == 3 and mes == 11:
                            idade.append((2022 - ano) +1)

                        else:
                            idade.append(2022 - ano)

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


with open(f'C:\\curso01_github\\seccao13\\arquivos_de_texto\\{nomeSaida}.txt','a+')as arquivoSaida:
    linhasTotais = lerArquivo1.split('\n')

    for l in range(0,len(linhasTotais)-1):
        # divide os nomes das datas
        nomes = linhasTotais[l].split()
        arquivoSaida.write(nomes[0] + ' ')

        
        arquivoSaida.write(str(idade[l]) + '\n')
        