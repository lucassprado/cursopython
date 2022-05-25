"""
Operadores Relacionais
== > >= < <= !=
"""

var_1 = 3
var_2 = 1
expressao = var_1 == var_2

print(expressao)

nome = input('Qual é o seu nome? ')
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
