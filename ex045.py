from random import choice
from time import sleep
print('--' * 20)
print('Vamos jogar jokenpo??')
eu = str(input('escolha pedra, papel ou tesoura: '))
eu = eu.lower()
print('--' * 20)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('POOO!!!')
print('--' * 20)
sleep(1)
lista = ('pedra', 'papel', 'tesoura')
computador = choice(lista)
print('Voce mostrou: {}'.format(eu))
print('O computador mostrou: {}'.format(computador))
print('__' * 20)
#player1
if eu == 'pedra' and computador == 'tesoura':
    print('Eu ganhei treine mais, sou melhor que uma maquina!!')
elif eu == 'tesoura' and computador == 'papel':
    print('Eu ganhei treine mais, sou melhor que uma maquina!!')
elif eu == 'papel' and computador == 'pedra':
    print('Eu ganhei, treine mais, sou melhor que uma maquina!!')
#computador
elif computador == 'papel' and eu == 'pedra':
    print('HAHAHAHA TREINE MAIS JOVEM GAFANHOTO, NÃO É CAPAZ DE VENCER MEU SISTEMA!!!')
elif computador == 'pedra' and eu == 'tesoura':
    print('HAHAHAHA TREINE MAIS JOVEM GAFANHOTO, NÃO É CAPAZ DE VENCER MEU SISTEMA!!!')
elif computador == 'tesoura' and eu == 'papel':
    print('HAHAHAHA TREINE MAIS JOVEM GAFANHOTO, NÃO É CAPAZ DE VENCER MEU SISTEMA!!!')
#empate
elif eu == 'pedra' and computador == 'pedra':
    print('Que pena deu empate!')
elif eu == 'papel' and computador == 'papel':
    print('Que pena deu empate!')
elif eu == 'tesoura' and computador == 'tesoura':
    print('Que pena deu empate!')
else:
    print('Você escreveu errado')
print('Vamos jogar novamente!!')
print('--' * 20)
