import re
import os

def clearScreen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def inputConsistente(perguntaInput, tipoDado):
    dado = ''
    while dado == '':
        clearScreen()
        if tipoDado == 'str':
            dadoTemp = input(f'\n{perguntaInput}')
            if re.match(r'^[A-Za-z]+( [A-Za-z]+)*$', dadoTemp):
                dado = dadoTemp
                return dado
            else:
                clearScreen()
                print('\nDigite um texto válido.\n')
                input('Pressione ENTER para digitar novamente.')
                dado = ''
        elif tipoDado == 'sexo':
            dadoTemp = input(f'\n{perguntaInput}')
            if len(dadoTemp) == 1 and dadoTemp in ['m', 'M', 'f', 'F'] :
                dado = dadoTemp
                return dado
            else:
                clearScreen()
                print('\nDigite um texto válido.\n')
                input('Pressione ENTER para digitar novamente.')
                dado = ''
        elif tipoDado == 'int':
            dadoTemp = input(f'\n{perguntaInput}')
            if re.match(r'^\d+$', dadoTemp):
                dado = int(dadoTemp)
                return dado
            else:
                clearScreen()
                print('\nDigite um valor válido.')
                input('Pressione ENTER para digitar novamente.')
                dado = ''
        elif tipoDado == 'cpf':
            dadoTemp = input(f'\n{perguntaInput}')
            if re.match(r'^\d+$', dadoTemp) and len(dadoTemp) == 11:
                dado = int(dadoTemp)
                return dado
            else:
                clearScreen()
                print('\nDigite um valor válido.')
                input('Pressione ENTER para digitar novamente.')
                dado = ''
        elif tipoDado == 'idade':
            dadoTemp = input(f'\n{perguntaInput}')
            if re.match(r'^\d+$', dadoTemp) and len(dadoTemp) > 0 and len(dadoTemp) <= 3:
                dado = int(dadoTemp)
                return dado
            else:
                clearScreen()
                print('\nDigite um valor válido.')
                input('Pressione ENTER para digitar novamente.')
                dado = ''
        elif tipoDado == 'float':
            dadoTemp = input(f'\n{perguntaInput}')
            if re.match(r'^\d+(\.\d+)?$', dadoTemp):
                dado = float(dadoTemp)
                return dado
            else:
                clearScreen()
                print('\nDigite um valor válido.')
                input('Pressione ENTER para digitar novamente.')
                dado = ''

def criarAtendimento(cartãoSUS, data):
    clearScreen()
    if cartãoSUS in data:
        clearScreen()
        print('\nJá existe um atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        nm = inputConsistente('Nome do paciente: ', 'str')
        cpf = inputConsistente('CPF do paciente: ', 'cpf')
        idade = inputConsistente('Idade do paciente: ', 'idade')
        sexo = inputConsistente('Sexo do paciente (M/F): ', 'sexo')
        sintomas = inputConsistente('Sintomas do paciente: ', 'str')
        convênio = inputConsistente('Convênio do paciente: ', 'str')

        data.update({cartãoSUS: [nm, cpf, idade, sexo, sintomas, convênio]})
        print(f'\nAtendimento criado com sucesso.\n')

def editarAtendimento(cartãoSUS,data):
    clearScreen()
    if cartãoSUS not in data:
        print('\nNão existe um atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        print(f'\nDigite em seguida a alteração dos dados relacionados ao cartão do SUS de número: {cartãoSUS}')

        nm = inputConsistente('Nome do paciente: ', 'str')
        cpf = inputConsistente('CPF do paciente: ', 'cpf')
        idade = inputConsistente('Idade do paciente: ', 'idade')
        sexo = inputConsistente('Sexo do paciente (M/F): ', 'sexo')
        sintomas = inputConsistente('Sintomas do paciente: ', 'str')
        convênio = inputConsistente('Convênio do paciente: ', 'str')

        data.update({cartãoSUS: [nm, cpf, idade, sexo, sintomas, convênio]  })

def encerrarAtendimento(cartãoSUS, data):
    clearScreen()
    if cartãoSUS not in data:
        print('\nNão existe atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    else:
        data.pop(cartãoSUS)
        
def pesquisaAtendimento(cartãoSUS, data):
    clearScreen()
    print('\nRegistro(s) de Cartão do SUS de acordo com o nome informado:\n')
    
    if cartãoSUS in data:
        print(f'\nCartão do SUS: {cartãoSUS} | Nome: {data[cartãoSUS][0]} | CPF: {data[cartãoSUS][1]} | Idade: {data[cartãoSUS][2]} | Sexo: {data[cartãoSUS][3]} | Sintomas: {data[cartãoSUS][4]} | Convênio: {data[cartãoSUS][5]}\n')
    else:
        print('\nNenhum registro encontrado.')
    
    input('\nDigite ENTER para continuar.')

def relatórioGeral(data):
    clearScreen()
    if len(data) == 0:
        print('\nNenhum registro encontrado.')
        input('\nPressione ENTER para voltar ao menu.')
    else:
        for cartãoSUS, dados in data.items():
            print(f'\nCartão do SUS: {cartãoSUS} | Nome: {dados[0]} | CPF: {dados[1]} | Idade: {dados[2]} | Sexo: {dados[3]} | Sintomas: {dados[4]} | Convênio: {dados[5]}\n')
        
        input('\nPressione ENTER para voltar ao menu.')
