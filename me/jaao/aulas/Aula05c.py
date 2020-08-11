# inputs
inicio = int(input('Qual o valor inicial? '))
final = int(input('Qual o valor final? '))
opcao = input('Digite P para saber os pares e I para os impares. ')
resultado = 0

for n in range(inicio, final + 1):
    if opcao == 'P' or opcao == 'p':
        if n % 2 == 0:
            resultado = resultado + 1
            print(n)
    if opcao == 'i' or opcao == 'I':
        if n % 2 == 1:
            resultado = resultado + 1
            print(n)

print('A quantidade é de:', resultado, 'números')
