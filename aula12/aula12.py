"""
Operadores lógicos
and, or, not
in e not in
"""

usuario = input('Usuário: ')
senha = input('Senha: ')

usuario_bd = 'lucas'
senha_bd = 'lucas123'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema.')
else:
    print('Usuário ou senha inválidos.')

if 'lu' in usuario_bd:
    print('As letras lu estão no nome do usuário.')
else:
    print('As letras não estão no nome do usuário.')

if 'pe' not in usuario_bd:
    print('As letras lu não estão no nome do usuário.')
else:
    print('As letras estão no nome do usuário.')
