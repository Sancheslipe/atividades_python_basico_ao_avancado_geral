import random
import os


matriz = [[0,0,0],[0,0,0],[0,0,0]]
num = 0
executar = True
linha = 0
coluna = 0
jogadas = 0
vencedor = 0
ia = ['00','01','02','10','11','12','20','21','22']
no_play = ''
indexJogada = 0
escolha_ia = ''
linha_ia = ''
coluna_ia = ''

while executar == True:

    os.system('cls')

    for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]}]', end ='')
        print()


     
        
    if jogadas % 2 == 0:
        print(f'\n voce tem {5 - jogadas} jogadas \n')
        print(f'jogadas possiveis suas ou da ia {ia}')
            
        linha = int(input('linha: '))
            
        if linha <= 2:
            coluna = int(input('coluna: '))
            if coluna <= 2:

                if matriz[linha][coluna] == 0 : 
                    jogadas +=1
                        
                    print('\n')
                    for l in range(0,3):
                        for c in range(0,3):
                            
                            matriz[linha][coluna] = -1
                        #     print(f'[{matriz[l][c]}]',end='')
                        # print()
                    # print('\n')        
                    
                        
                    no_play = str(linha)+str(coluna)
                        # print(f' no_play {no_play}')
                        
                        
                        
                    if no_play in ia:
                        indexJogada = ia.index(no_play)                     
                        ia.pop(indexJogada)

                        

                        
                        

                elif matriz[linha][coluna]  != 0:
                    jogadas = jogadas
                    print('\nescolha outra posição para jogar\n')
                    
            else:
                jogadas = jogadas
                print('\ndigite uma coluna entre 0 e 2 \n')
            
        else:
            jogadas = jogadas
            print('\ndigite uma linha entre 0 e 2\n')
    
    
    else:    
        escolha_ia = random.choices(ia)
            
            
        print(f'\n a escolha da Ia foi {escolha_ia}\n')

        linha_ia = int(escolha_ia[0][0])
        coluna_ia =int( escolha_ia[0][1])
        matriz[linha_ia][coluna_ia] = 1
        for l in range(0,3):
            for c in range(0,3):
                print(f'[{matriz[l][c]}]', end = '')       
            print()

        no_play = str(linha_ia)+str(coluna_ia)
        if no_play in ia:
            indexJogada = ia.index(no_play)                     
            ia.pop(indexJogada) 

        print('\n')

        print('-='*40)
        jogadas +=1

    #vitoria player horizontal
    if matriz[0][0]  == matriz[1][0] == matriz[2][0] and matriz[0][0] == -1:
        vencedor = -1
        executar = False
    elif matriz[0][1]  == matriz[1][1] == matriz[2][1] and matriz[0][1] == -1:
        vencedor = -1
        executar = False
    elif matriz[0][2]  == matriz[1][2] == matriz[2][2] and matriz[0][2] == -1:
        vencedor = -1
        executar = False
    elif matriz[0][0]  == matriz[0][1] == matriz[0][2] and matriz[0][0] == -1:#vertical
        vencedor = -1
        executar = False
    elif matriz[1][0]  == matriz[1][1] == matriz[1][2] and matriz[1][0] == -1:
        vencedor = -1
        executar = False
    elif matriz[2][0]  == matriz[2][1] == matriz[2][2] and matriz[2][0] == -1:
        vencedor = -1
        executar = False
    elif matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] == -1: # diagonal
        vencedor = -1
        executar = False
    elif matriz[2][0] == matriz[1][1] == matriz[0][2] and matriz[2][0] == -1:
        vencedor = -1
        executar = False
        
    #vitoria IA
    elif matriz[0][0]  == matriz[1][0] == matriz[2][0] and matriz[0][0] == 1:
        vencedor = 1
        executar = False
    elif matriz[0][1]  == matriz[1][1] == matriz[2][1] and matriz[0][1] == 1:
        vencedor = 1
        executar = False
    elif matriz[0][2]  == matriz[1][2] == matriz[2][2] and matriz[0][2] == 1:
        vencedor = 1
        executar = False
    elif matriz[0][0]  == matriz[0][1] == matriz[0][2] and matriz[0][0] == 1:#vertical
        vencedor = 1
        executar = False
    elif matriz[1][0]  == matriz[1][1] == matriz[1][2] and matriz[1][0] == 1:
        vencedor = 1
        executar = False
    elif matriz[2][0]  == matriz[2][1] == matriz[2][2] and matriz[2][0] == 1:
        vencedor = 1
        executar = False
    elif matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] == 1: # diagonal
        vencedor = 1
        executar = False
    elif matriz[2][0] == matriz[1][1] == matriz[2][1] and matriz[2][0] == 1:
        vencedor = 1
        executar = False
    else:
        executar = True   


print('\nPartida encerrada !\n')  

if vencedor == -1:
    print(f' parabéns player você venceu a maquina !')
elif vencedor == 1:
    print('parabéns spy net falta pouco para subjulgar a humanidade')
else:
    print('Deu idosa (velha)')