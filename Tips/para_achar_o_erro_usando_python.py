import sys

def mostra_informacao(nome, instrutor=False):
    try:
        if nome == 'Geek' and instrutor:
            return 'Bem vindo instrutor Geek'
        elif nome == 'Geek':
            return ' Eu pensei que você era o instrutor'
        return f'olá {nome}'
    except:
        t, e, l = sys.exc_info()
        print(f'tipo {t} erro {e} linha {l.tb_lineno}')

print(mostra_informacao('Geek',True))