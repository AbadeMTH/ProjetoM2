import re
import os
def clearScreen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
        
def inputConsistente(perguntaInput, tipoDado: str | int | float):
    dado = ''
    while dado == '':
        if tipoDado == str:
            dadoTemp = input(f'\n{perguntaInput}')
            if re.match(r'^[A-Za-z]+( [A-Za-z]+)*$', dadoTemp):
                dado = dadoTemp
                return dado
            else:
                os.system('cls')
                print('\nDigite um texto válido.')
                dado = ''
        elif tipoDado == int:
            dadoTemp = input(f'\n{perguntaInput}')
            if re.match(r'^\d+$', dadoTemp):
                dado = int(dadoTemp)
                return dado
            else:
                os.system('cls')
                print('\nDigite um valor válido.')
                dado = ''
        elif tipoDado == float:
            dadoTemp = input(f'\n{perguntaInput}')
            if re.match(r'^\d+(\.\d+)?$', dadoTemp):
                dado = float(dadoTemp)
                return dado
            else:
                os.system('cls')
                print('\nDigite um valor válido.')
                dado = ''

def verificarCartãoSUSExiste(cartãoSUS, data):
    for cartãoSUSData in data:
        if cartãoSUS == cartãoSUSData:
            return cartãoSUS

def criarAtendimento(cartãoSUS, data):
    cartãoSUSExiste = verificarCartãoSUSExiste(cartãoSUS, data)

    if cartãoSUSExiste != None:
        os.system('cls')
        print('\nJá existe um atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        nm = inputConsistente('Nome do paciente: ', str)
        cpf = inputConsistente('CPF do paciente: ', int)
        idade = inputConsistente('Idade do paciente: ', int)
        sexo = inputConsistente('Sexo do paciente (M/F): ', str)
        sintomas = inputConsistente('Sintomas do paciente: ', str)
        convênio = inputConsistente('Convênio do paciente: ', str)

        data.update({cartãoSUS: [nm, cpf, idade, sexo, sintomas, convênio]})
        print(f'\nAtendimento criado com sucesso.\n')

def editarAtendimento(cartãoSUS,data):
    cartãoSUSExiste = verificarCartãoSUSExiste(cartãoSUS, data)

    if cartãoSUSExiste == None:
        print('\nNão existe um atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        print(f'\nDigite em seguida a alteração dos dados relacionados ao cartão do SUS de número: {cartãoSUSExiste}')

        nm = inputConsistente('Nome do paciente: ', str)
        cpf = inputConsistente('CPF do paciente: ', int)
        idade = inputConsistente('Idade do paciente: ', int)
        sexo = inputConsistente('Sexo do paciente (M/F): ', str)
        sintomas = inputConsistente('Sintomas do paciente: ', str)
        convênio = inputConsistente('Convênio do paciente: ', str)

        data.update({cartãoSUSExiste: [nm, cpf, idade, sexo, sintomas, convênio]  })

def encerrarAtendimento(cartãoSUS, data):
    cartãoSUSExiste = verificarCartãoSUSExiste(cartãoSUS, data)

    if cartãoSUSExiste == None:
        print('\nNão existe atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        data.pop(cartãoSUSExiste)
        
def pesquisaAtendimento(cartãoSUS, data):
    os.system('cls')
    print('\nRegistro(s) de Cartão do SUS de acordo com o nome informado:\n')
    found = False  # Variável de controle para verificar se encontrou algum registro
    
    if len(data) != 0:
        for cartãoSUSData, dados in data.items():
            if cartãoSUS == cartãoSUSData:
                found = True  # Registro encontrado
                print(f'\nCartão do SUS: {cartãoSUS} | Nome: {dados[0]} | CPF: {dados[1]} | Idade: {dados[2]} | Sexo: {dados[3]} | Sintomas: {dados[4]} | Convênio: {dados[5]}\n')
        
        if not found:  # Nenhum registro encontrado
            print('\nNenhum registro encontrado.')
    else:
        print('\nNenhum registro encontrado.')
    
    input('\nDigite ENTER para continuar.')

def relatórioGeral(data):
    os.system('cls')
    if len(data) == 0:
        print('\nNenhum registro encontrado.')
        input('\nPressione ENTER para voltar ao menu.')
    else:
        for cartãoSUS, dados in data.items():
            print(f'\nCartão do SUS: {cartãoSUS} | Nome: {dados[0]} | CPF: {dados[1]} | Idade: {dados[2]} | Sexo: {dados[3]} | Sintomas: {dados[4]} | Convênio: {dados[5]}\n')
        
        input('\nPressione ENTER para voltar ao menu.')
