values = [102, 5, 76, 900, 80, 2, 74]

element = min(values)

for i in range(len(values)):
    if values[i] == element:
        print('O menor elemento da lista é: {}, e sua posição na lista é: {}'
              .format(element, i))
