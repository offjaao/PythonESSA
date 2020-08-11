# Template para conversão: Celsius = ((Fahrenheit - 32) * 5) / 9

fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
celsius = ((fahrenheit - 32) * 5) / 9
print(fahrenheit, 'ºF em Celsius é: {:.1f}'.format(celsius), 'ºC')
