from time import sleep
from random import randint
print('--__--' * 20)
print('seja bem! Aqui começa um novo desafio.')
sleep(3)
print('Será que você conseguirá me vencer?')
sleep(2)
print('Irá funcionar da seguinte forma... Você precisa acertar o codigo que desarma'
      ' a bomba que está localizada no')
print('centro de New York. Será que você consegue?!')
print('--__--' * 20)
sleep(2)
print('vamos la...')
sleep(3)
print('==+=='*20)
print('O codigo esta dentro de uma tabela de senhas entre 0 e 5...')
print('Você precisa ser rapido para descobrir... só temos uma hora! corra!')
computador = randint(0,5)
computador2 = randint(0,5)
computador3 = randint(0,5)
jogador = int(input('digite o codigo com 3 numeros:'))
print('PROCESSANDO...')
sleep(4)
if jogador == computador == computador3 == computador2:
      print('Explendido! Você, conseguiu savar New York! os cidadãos estão salvos por sua causa, BOM TRABALHO!')
else:
      print('Infelizmente Você errou... A cidade de New York foi destruida, o codigo era: {}{}{}'.format(computador,computador2,computador3))
print('==+=='*20)
