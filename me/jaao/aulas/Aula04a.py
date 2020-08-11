ano = int(input('Qual o ano que você nasceu? Ex: 2003'))
idade = 2020 - ano
# print(idade)

print('Você é menor de idade' if idade < 18 else 'Você é maior de idade')


# if idade < 18:
#    print('Você é menor de idade')
# else:
#    print('Você é maior de idade')
