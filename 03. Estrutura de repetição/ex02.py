while True:
    nick = input('Digite seu nome de usuario: ')
    senha = input('Digite sua senha: ')
    if nick == senha:
        print('Senha INVALIDA')
        continue
    else:
        print(f'Acesso permitido, bem vindo(a), {nick}')
        break