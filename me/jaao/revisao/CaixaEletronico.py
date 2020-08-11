valor = int(input('Qual o valor desejado? '))

qnt50 = valor // 50
resto = valor % 50
print('Quantidades de nota de R$50', qnt50)

qnt20 = resto // 20
resto = resto % 20
print('Quantidades de nota de R$20', qnt20)

qnt10 = resto // 10
resto = resto % 10
print('Quantidades de nota de R$10', qnt10)

qnt5 = resto // 5
resto = resto % 5
print('Quantidades de nota de R$5', qnt5)

qnt2 = resto // 2
resto = resto % 2
print('Quantidades de nota de R$5', qnt2)
print('Resto:', resto)
