av1 = float(input('Digite a nota da avaliação 1?'))
av2 = float(input('Digite a nota da avaliação 2?'))
av3 = float(input('Digite a nota da avaliação 3?'))

media = (av1 + av2 + av3) / 3
print(media)

if media < 5:
    print('Reprovado')
elif media > 8:
    print('Aprovado com louvor')
else:
    print('Aprovado')
