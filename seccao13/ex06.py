with open('C:\\Curso01\\seccao13\\arquivos_de_texto\\ex01.txt')as arquivo:
    paginasTotais = arquivo.readlines()
    letraA = 0
    letraB = 0 
    letraC = 0 
    letraD = 0 
    letraE = 0 
    letraF = 0 
    letraG = 0 
    letraH = 0 
    letraI = 0 
    letraJ = 0 
    letraK = 0 
    letraL = 0 
    letraM = 0 
    letraN = 0 
    letraO = 0 
    letraP = 0 
    letraQ = 0 
    letraR = 0 
    letraS = 0 
    letraT = 0 
    letraU = 0 
    letraV = 0 
    letraW = 0 
    letraX = 0 
    letraY = 0 
    letraZ = 0

    for l in range(len(paginasTotais)):
        palavra = paginasTotais[l].lower()
        for i in range(len(palavra)): 
            
            if 'a' == palavra[i]:
                letraA += 1
            elif 'b' == palavra[i]:
                letraB += 1
            elif 'c' == palavra[i]:
                letraC += 1
            elif 'd' == palavra[i]:
                letraD += 1
            elif 'e' == palavra[i]:
                letraE += 1
            elif 'f' == palavra[i]:
                letraF += 1
            elif 'g' == palavra[i]:
                letraG += 1
            elif 'h' == palavra[i]:
                letraH += 1
            elif 'i' == palavra[i]:
                letraI += 1
            elif 'j' == palavra[i]:
                letraJ += 1
            elif 'k' == palavra[i]:
                letraK += 1
            elif 'l' == palavra[i]:
                letraL += 1
            elif 'm' == palavra[i]:
                letraM += 1
            elif 'n' == palavra[i]:
                letraN += 1
            elif 'o' == palavra[i]:
                letraO += 1
            elif 'p' == palavra[i]:
                letraP += 1
            elif 'q' == palavra[i]:
                letraQ += 1
            elif 'r' == palavra[i]:
                letraR += 1
            elif 's' == palavra[i]:
                letraS += 1
            elif 't' == palavra[i]:
                letraT += 1
            elif 'u' == palavra[i]:
                letraU += 1
            elif 'v' == palavra[i]:
                letraV += 1
            elif 'w' == palavra[i]:
                letraW += 1
            elif 'x' == palavra[i]:
                letraX += 1
            elif 'y' == palavra[i]:
                letraY += 1
            elif 'z' == palavra[i]:
                letraZ += 1

print(f' a letra A aparece {letraA} vezes \n')  
print(f' a letra B aparece {letraB} vezes \n')  
print(f' a letra C aparece {letraC} vezes \n')  
print(f' a letra D aparece {letraD} vezes \n')  
print(f' a letra E aparece {letraE} vezes \n')  
print(f' a letra F aparece {letraF} vezes \n') 
print(f' a letra G aparece {letraG} vezes \n')  
print(f' a letra H aparece {letraH} vezes \n')  
print(f' a letra I aparece {letraI} vezes \n') 
print(f' a letra J aparece {letraJ} vezes \n')  
print(f' a letra K aparece {letraK} vezes \n')  
print(f' a letra L aparece {letraL} vezes \n') 
print(f' a letra M aparece {letraM} vezes \n')  
print(f' a letra N aparece {letraN} vezes \n')  
print(f' a letra O aparece {letraO} vezes \n')  
print(f' a letra P aparece {letraP} vezes \n')  
print(f' a letra Q aparece {letraQ} vezes \n')  
print(f' a letra R aparece {letraR} vezes \n') 
print(f' a letra S aparece {letraS} vezes \n')  
print(f' a letra T aparece {letraT} vezes \n')  
print(f' a letra U aparece {letraU} vezes \n') 
print(f' a letra V aparece {letraV} vezes \n')  
print(f' a letra W aparece {letraW} vezes \n')  
print(f' a letra X aparece {letraX} vezes \n') 
print(f' a letra Y aparece {letraY} vezes \n')  
print(f' a letra Z aparece {letraZ} vezes \n') 
