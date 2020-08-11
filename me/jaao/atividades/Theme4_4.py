# Desenvolva um programa que calcule e exiba a soma dos números pares contidos entre 1 e um número fornecido pelo
# usuário.

number = int(input('Digite um número: '))

for i in range(1, number):
    if i % 2 == 0:
        print(i)
