nome = 'Lucas Prado'
idade = 20
altura = 1.85
e_maior = idade > 18
peso = 75
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade e seu IMC é {imc}')
print('{} tem {} anos e seu IMC é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos e seu IMC é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu IMC é {im:.2f}'.format(n=nome, i=idade, im=imc))
