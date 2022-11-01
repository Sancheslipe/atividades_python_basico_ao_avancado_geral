'''
OBS: Ao abrir um arquivo para leitura, não pidenis escrever nele, apenas ler.
OBS: Ao abrir um arquivo para esctira, o arquivo é criado no nosso sistema operacional
Para escrevermos dados em um arquivo, após abrir o arquivo uilizamos a função write().
 Esta função recebe uma string como parametro

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.

'''

with open('C:\\Curso01\\seccao13\\cafe.txt','w') as arquivo:
    arquivo.write('Mensagens subliminares não são legais \n' * 150)
    