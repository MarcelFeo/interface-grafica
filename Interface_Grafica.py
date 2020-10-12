import PySimpleGUI as sg

class Tela:
    def __init__(self):
        sg.change_look_and_feel('LightBlue7')
        #Layout
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Cidade', size=(5, 0)), sg.Input(size=(15, 0), key='cidade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Qual o seu sexo?')],
            [sg.Radio('Masculino', 'sexo', key='masculino'), sg.Radio('Feminino', 'sexo', key='feminino')],
            [sg.Button('Enviar'), sg.Cancel()],
            [sg.Output(size=(30, 20))]
        ]
        #Window
        self.window = sg.Window("Dados do Usuário").layout(layout)
        #Dados
        self.button, self.values = self.window.Read()

    def Start(self):
        while True:
            self.button, self.values = self.window.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            cidade = self.values['cidade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            masculino = self.values['masculino']
            feminino = self.values['feminino']
            slider = self.values['slider']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'cidade: {cidade}')
            print(f'gmail: {aceita_gmail}')
            print(f'outlook: {aceita_outlook}')
            print(f'yahoo: {aceita_yahoo}')
            print(f'masculino: {masculino}')
            print(f'feminino: {feminino}')


tela = Tela()
tela.Start()