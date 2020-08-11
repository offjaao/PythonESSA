valores = [11, 48, 45, 14, 72, 74, 27, 6, 12]

soma = 0

for n in range(len(valores)):
    if n % 2 == 0:
        print('O indice {}, armazena o valor {}'.format(n, valores[n]))
        soma = soma + valores[n]
print(soma)
