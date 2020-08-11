# Repetição com while #

# n = 0
# while n < 10:
#    print(n)
#   n = n + 1

import random

numero = random.randint(1, 100)
aposta = 0
tentativas = 0

while aposta != numero:
    # print(numero)
    aposta = int(input('Qual o número que estou pensando? '))
    tentativas = tentativas + 1
    if aposta > numero:
        print('Sua aposta foi muito alta!')

    if aposta < numero:
        print('Sua aposta foi muito baixa!')

print('Você acertou o número em', tentativas, 'apostas!')
