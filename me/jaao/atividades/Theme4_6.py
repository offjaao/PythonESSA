# Desenvolva um programa que leia valores inteiros e encontre o maior e o menor deles. Termine
# a leitura se o usuário digitar zero (0)

numbers = []

while True:
    valor = int(input('Digite um número, para sair digite 0: '))
    if valor != 0:
        numbers.append(valor)
    elif valor == 0:
        if not numbers:
            print('Nenhum valor encontrado na lista.')
        else:
            print('Maior valor: ', max(numbers))
            print('Menor valor: ', min(numbers))
        break
