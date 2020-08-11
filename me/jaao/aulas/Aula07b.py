import PySimpleGUI as pSG

# criando a tela 1
tela1 = [[pSG.Text('Hello World!')],
         [pSG.Text('Tela desenvolvida com o uso da biblioteca PySimpleGUI')]]

# mostrar a tela
janela = pSG.Window('Titulo: Aula07b', tela1)

janela.read()
