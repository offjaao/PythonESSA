def sUnidade():
    unidade = input('Para qual unidade deseja converter? C - Celsius / F - Fahrenheit ')
    valor = float(input('Qual a temperatura? '))

    if unidade == 'f':
        cParaF(valor)

    elif unidade == 'c':
        fParaC(valor)

    else:
        print('Unidade não encontrada')
        sUnidade()


def cParaF(valor):
    f = ((valor * 9) / 5) + 32
    print('A temperatura em fahrenheit é de {:.1f}'.format(f))

def fParaC(valor):
    c = ((valor - 32) * 5) / 9
    print('A temperatura em celsius é de {:.1f}'.format(c))


sUnidade()
