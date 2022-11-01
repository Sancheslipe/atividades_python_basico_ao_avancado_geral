# VALIDAÇÃO PARA SABER SE O USUÁRIO UTILIZOU FLOAT, POSITIVOS OU QULQUER OUTRA COISA
num1 = input('digite um numero')


if num1.replace(".", "", 1).isdigit():
    num1 = float(num1)
    print(num1)
else:
    print('não rodou')

# VALIDAÇÃO PARA SABER SE O USUÁRIO UTILIZOU FLOAT, POSITIVOS/NEGATIVOS , OU QULQUER OUTRA COISA
num1 = input('digite um numero')


if num1.replace(".", "", 1).replace('-', '').isdigit():
    num1 = float(num1)
    print(num1)
else:
    print('não rodou')
