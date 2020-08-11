import random

alternativas = ('Pedra', 'Papel', 'Tesoura')
print('Suas opções são: 0 - Pedra, 1 - Papel e 2 Tesoura')
jogador = int(input('Escolha a sua opção: '))
print('Você escolheu:', alternativas[jogador])
computador = random.randint(0, 2)
print('O computador escolheu:', alternativas[computador])

# comparando
if computador == 0:
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Jogador ganhou!')
    elif computador == 2:
        print('Computador ganhou!')

if computador == 1:
    if jogador == 0:
        print('Computador ganhou!')
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2:
        print('Jogador ganhou!')

if computador == 2:
    if jogador == 0:
        print('Jogador ganhou!')
    elif jogador == 1:
        print('Computador ganhou')
    elif jogador == 2:
        print('Empatou')
