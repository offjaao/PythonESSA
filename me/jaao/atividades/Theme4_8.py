# Desenvolva um programa que calcule a soma de todos os números primos existentes entre 1
# e 100.

numbers = [x for x in range(101)]
prime = []
div = [x for x in numbers if x != 0]

for i in numbers:
    calc = 0
    for j in div:
        if i % j == 0:
            calc += 1
        elif i < j:
            break
    if calc == 2:
        prime.append(i)

print(prime)
