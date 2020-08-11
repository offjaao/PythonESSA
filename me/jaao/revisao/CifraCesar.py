alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', ' ']
tamLista = len(alfabeto)
mensagemNum = []

mensagem = input('Digite sua mensagem: ')
mensagem2 = mensagem.upper()

cripto = 3
segredo = ''

for n in range(len(mensagem2)):
    valor = mensagem2[n]
    for i in range(tamLista):
        if alfabeto[i] == valor:
            mensagemNum.append(i)
            # print(i)
# pegando mensagem e mostrando criptografada
for c in range(len(mensagemNum)):
    novo = cripto + mensagemNum[c]
    if novo <= tamLista:
        segredo += alfabeto[novo]
    elif novo > tamLista:
        novo -= tamLista
        segredo += alfabeto[novo]
    # print(alfabeto[novo])

print(segredo)
