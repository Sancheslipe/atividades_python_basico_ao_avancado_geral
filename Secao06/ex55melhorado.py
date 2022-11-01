cont = input('digite um numero')
primo = False
i = 2
soma = 0 

if (cont.isdigit()) and int(cont) > 0:
    
    cont = int(cont)

    while i <= cont:

        if (i != 2 ) and (i % 2 ==0): 
            primo = False
            
        elif (i !=3) and (i % 3 == 0):
            primo = False
        else:
            primo = True
        
        if primo == True:
            soma = soma + i
            print(i)
        i = i + 1
# fazer por 1 e ele mesmo

    print(f' a soma é {soma}')
else:
    print('digite um numero válido')
