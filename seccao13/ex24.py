import pickle
vetor = ['felipe', '18', 'café','agua','testi']
arq = open(f'C:\\Curso01\\seccao13\\arquivos_de_texto\\texto.pkl','wb')
    
arq.write(pickle.dumps(vetor))
