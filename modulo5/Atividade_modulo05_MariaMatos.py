def realizar_logiin():
    '''
    função que simula uma tela de login capturando nome e senha.
    '''

    print('\nTela de login - Meet\n')

    nome_usuario = input('Digite seu login para continuar: ')
    senha_usuario = input('Digite sua senha para continuar: ')

    print(f'Bem-vindo, {nome_usuario}!')

    print('---------------------------\n')
    
    realizar_login()