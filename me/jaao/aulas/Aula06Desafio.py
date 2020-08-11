# imports
import random

# vars
disponiveis = []
sorteados = []


# funcs
def sorteio():
    sorte = random.randint(0, len(disponiveis) - 1)
    print('Pedra nº', disponiveis[sorte])
    sorteados.append(disponiveis[sorte])
    disponiveis.pop(sorte)
    continuar = input('Deseja continuar (S/N)? ')
    if continuar == 's' or continuar == 'S':
        sorteio()
    elif continuar == 'n' or continuar == 'N':
        mostrarResultado()


def mostrarResultado():
    sorteados.sort()
    print(sorteados)
    voltar = input('Deseja voltar ao sorteio (S/N)? ')
    if voltar == 's' or voltar == 'S':
        sorteio()


# sort
for n in range(1, 76):
    if 1 <= n < 15:
        disponiveis.append('B' + str(n))
    elif 15 <= n < 31:
        disponiveis.append('I' + str(n))
    elif 30 <= n < 46:
        disponiveis.append('N' + str(n))
    elif 45 <= n < 61:
        disponiveis.append('G' + str(n))
    elif 60 <= n < 76:
        disponiveis.append('O' + str(n))

# sorteando
inicio = input('Deseja começar (S/N)? ')
if inicio == 's' or inicio == 'S':
    sorteio()
