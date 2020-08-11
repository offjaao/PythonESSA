value = int(input('Qual o valor do produto desejado? '))
percent = int(input('Qual o valor da porcentagem (%) desejada? '))

percentCalc = value * percent / 100
newValue = value - percentCalc

print('---------=========#########=========---------')
print('O valor original do produto é de: R${}\n'
      'O valor do desconto à ser aplicado é de: {}%\n'
      'O valor com o desconto passa a ser de: R${}\n'
      'Com isso, você irá economizar: R${}'
      .format(value, percent, newValue, percentCalc))
print('---------=========#########=========---------')
