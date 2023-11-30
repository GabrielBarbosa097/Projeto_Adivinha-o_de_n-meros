import random

print('BEM VINDO AO JOGO DE ADIVINHAÇÃO')
print('-='*20)
input('Aperte ENTER para começar')
print('-='*20)
print('INICIANDO O JOGO DE ADIVINHAÇÃO')


numeros = random.randint(1,100)
acertou = False
jogar_novamente = 's'

while not acertou:
    jogador = int(input('Digite um numero de 1 a 100: '))
    if jogador > numeros:
        print('Tente um numero menor')
    elif jogador < numeros:
        print('Tente um numero maior')
    else:
        print(f'Parabéns, Você acertou o numero escolhido que no caso foi {numeros}')
        jogar_novamente = input('Jogo encerrado, deseja jogar novamente? [S/N]').lower()
        if jogar_novamente == 's':
            continue
        else:
            break
print('-='*20)
print('JOGO ENCERRADO, OBRIGADO POR JOGAR!!!!')
print('-='*20)
