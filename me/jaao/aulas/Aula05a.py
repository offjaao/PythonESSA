# Repetição Simples#

for n in range(10):
    print(n)

# Repetição com variáveis

inicio = 1
final = 12
for n in range(inicio, final + 1):
    print(n)

# Repetição regressiva

inicio = 12
final = 9
passo = -1

for n in range(inicio, final + 1, passo):
    print(n)

# Repetição pedindo valores

inicio = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor do final: '))
passo = int(input('Digite o valor do passo: '))

for n in range(inicio, final, passo):
    print(n)
