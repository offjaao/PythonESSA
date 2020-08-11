# calculo


# menu
def menu(resposta):
    if resposta == 's' or resposta == 'S':
        sNotas()
    else:
        print('Cancelado.')


# solicitando notas
def sNotas():
    av1 = float(input('Qual o valor da avaliação 1? '))
    av2 = float(input('Qual o valor da avaliação 2? '))
    av3 = float(input('Qual o valor da avaliação 3? '))
    cNotas(av1, av2, av3)


# calculando a média
def cNotas(av1, av2, av3):
    media = (av1 + av2 + av3) / 3
    mNotas(media)


# mostrando notas
def mNotas(media):
    print('Sua média é: ', media)
    resposta = input('Deseja calcular outra média? ')
    menu(resposta)


# executar
sNotas()
