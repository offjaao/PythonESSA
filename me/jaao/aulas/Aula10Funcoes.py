def parImpar(num):
    if num % 2 == 0:
        print('O valor {} é Par'.format(num))
    else:
        print('O valor {} é Impar'.format(num))


def primos(num):
    contador = 0
    for n in range(1, num + 1):
        if num % n == 0:
            contador += 1
    if contador == 2:
        print('O valor {} é um número primo.'.format(num))
    else:
        print('O valor {} não é um número primo.'.format(num))
