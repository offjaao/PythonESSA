valores = [11, 48, 45, 14, 72, 74, 27, 6, 12]

soma = 0

for n in range(len(valores)):
    if valores[n] % 2 != 0:
        print('O valor é: {}'.format(valores[n]))
        soma = soma + valores[n]
print('O total de todos os elementos impares é: {}'.format(soma))
