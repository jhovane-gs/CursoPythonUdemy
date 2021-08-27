nome = 'YoungJho'
idade = 17 # int 
altura = 1.65 # float
e_maior = idade > 18 #bool
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {} '.format(nome, idade, imc))
