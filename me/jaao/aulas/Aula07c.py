import PySimpleGUI as gui


def screen():
    layout = [
        [gui.Text('Qual o valor do Produto', size=(18, 0)), gui.Input(key='valor')],
        [gui.Text('Qual a % do desconto', size=(18, 0)), gui.Input(key='desconto')],
        [gui.Text('O valor do desconto é:', size=(18, 0))],
        [gui.Text('O valor final do produto é:', size=(18, 0))],
        [gui.Button('Calcular'), gui.Button('Sair')]
    ]
    window = gui.Window('Calculadora de Descontos', layout)
    event, values = window.read()
    readValues(values)


def readValues(values):
    # print(values)
    # print(float(values['valor']))
    # print(float(values['desconto']))
    value = float(values['valor'])
    discount = float(values['desconto'])
    calculated = value * (discount / 100)
    result = value - calculated


screen()