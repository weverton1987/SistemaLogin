from Controller import ControllerCadastro, ControllerLogin
while True:
    print('='*10, 'menu', '='*10)
    decidir = input(
        'Digite 1 para cadastrar\nDigite 2 para logar\nDigite 3 para sair\n')
    if decidir == 1:
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        resultado = ControllerCadastro.cadastrar(nome, email, senha)
        if resultado == 2:
            print('Tamanho do nome inválido.')
    if decidir == 2:
        ...
    else:
        ... 