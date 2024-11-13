import os
import re

ListaDados = []
DicionárioPacientes = {}
def clearScreen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def getDados():
    try:
        with open("dados.txt", "r", encoding="utf-8") as dados:
            for linha in dados:
                ListaDados.append(linha.rstrip().split('|')) #rstrip() remove todos caracteres de controle a direita e split(',') separa os dados pela vírgula
            
            for dado in ListaDados:
                DicionárioPacientes[int(dado[0])] = [dado[1], int(dado[2]), int(dado[3]), dado[4], dado[5], dado[6]] #passando dados da lista para dicionário
            
            return DicionárioPacientes
    except FileNotFoundError:
        return {}

def saveDados(data):
    with open('dados.txt', 'w', encoding='utf8') as dadosTXT:
        for chave, dados in data.items():
            dadosTXT.write(f"{chave}|{dados[0]}|{dados[1]}|{dados[2]}|{dados[3]}|{dados[4]}|{dados[5]}\n")
    

def inputConsistente(perguntaInput, tipoDado):
    while True:
        clearScreen()
        print("\033[1;34m╔════════════════════════════════════════════════════════════════╗\033[m")
        print(f"\033[1;34m   🏥 {perguntaInput}                                           \033[m")
        print("\033[1;34m╚════════════════════════════════════════════════════════════════╝\033[m")
        
        dadoTemp = input(f'\033[1;32m📝 Digite: \033[m')
        
        if tipoDado == 'str' and re.match(r'^[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ]+( [A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ]+)*$', dadoTemp) and len(dadoTemp) <= 50: #Regex aceita apenas letras com ou sem acentos ou cedilhas sem espaços no início e finall
            return dadoTemp
        elif tipoDado == 'sexo' and dadoTemp.lower() in ['m', 'f']:
            return 'Masculino' if dadoTemp.lower() == 'm' else 'Feminino'
        elif tipoDado == 'cancelar' and dadoTemp.lower() in ['s', 'n']:
            return 'sim' if dadoTemp.lower() == 's' else 'não'
        elif tipoDado == 'int' and dadoTemp.isdigit():
            return int(dadoTemp)
        elif tipoDado == 'cpf' and dadoTemp.isdigit() and len(dadoTemp) == 11:
            return dadoTemp
        elif tipoDado == 'idade' and dadoTemp.isdigit() and 0 < int(dadoTemp) < 120:
            return int(dadoTemp)
        elif tipoDado == 'sintomas' and re.match(r'^[A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ.,;:\- ]+( [A-Za-záàãâäéèêëíìîïóòôöõúùûüçÇ.,;:\- ]+)*$', dadoTemp) and len(dadoTemp) <= 180:
            return dadoTemp
        else:
            print('\n❌ Valor inválido.\n')
            input('Pressione ENTER para tentar novamente.')

def criarAtendimento(cartaoSUS, data):
    clearScreen()
    print("\033[1;32m╔════════════════════════════════════════════════════════════╗ \033[m")
    print("\033[1;32m              🚑 Criar Novo Atendimento                           \033[m")
    print("\033[1;32m╚════════════════════════════════════════════════════════════╝ \033[m")
    if cartaoSUS in data:
        print('\n❌ Já existe um atendimento com esse cartão.\n')
        input('Pressione ENTER para voltar ao menu.')
    else:
        nome = inputConsistente('Nome do paciente: ', 'str')
        cpf = inputConsistente('CPF do paciente: ', 'cpf')
        idade = inputConsistente('Idade do paciente: ', 'idade')
        sexo = inputConsistente('Sexo do paciente (M/F): ', 'sexo')
        sintomas = inputConsistente('Diga brevemente os sintomas do paciente (180 caracteres): ', 'sintomas')
        convenio = inputConsistente('Convênio do paciente: ', 'str')
        confirmar = inputConsistente('Deseja confirmar o atendimento? (S/N): ', 'cancelar')
        
        if confirmar == 'não':
            print('\n❌ Atendimento cancelado com sucesso!')
        else:
            data[cartaoSUS] = [nome, cpf, idade, sexo, sintomas, convenio]
            print('\n✅ Atendimento criado com sucesso.')
        input('Pressione ENTER para voltar ao menu.')

def editarAtendimento(cartaoSUS, data):
    clearScreen()
    print("\033[1;33m╔════════════════════════════════════════════════════════════╗\033[m")
    print("\033[1;33m              ✏️ Editar Atendimento                           \033[m")
    print("\033[1;33m╚════════════════════════════════════════════════════════════╝\033[m")
    if cartaoSUS not in data:
        print('\n❌ Não existe um atendimento com esse cartão.\n')
        input('Pressione ENTER para voltar ao menu.')
    else:
        nome = inputConsistente('Altere o nome do paciente: ', 'str')
        cpf = inputConsistente('Altere o CPF do paciente: ', 'cpf')
        idade = inputConsistente('Altere a idade do paciente: ', 'idade')
        sexo = inputConsistente('Altere o sexo do paciente (M/F): ', 'sexo')
        sintomas = inputConsistente('Altere os sintomas do paciente: ', 'sintomas')
        convenio = inputConsistente('Altere o convênio do paciente: ', 'str')
        confirmar = inputConsistente('Deseja confirmar a alteração? (S/N): ', 'cancelar')
        
        if confirmar == 'não':
            print('\n❌ Alteração cancelada com sucesso!')
        else:
            data[cartaoSUS] = [nome, cpf, idade, sexo, sintomas, convenio]
            print('\n✅ Atendimento alterado com sucesso.')
        input('Pressione ENTER para voltar ao menu.')

def encerrarAtendimento(cartaoSUS, data):
    clearScreen()
    print("\033[1;31m╔════════════════════════════════════════════════════════════╗\033[m")
    print("\033[1;31m               ⚠️ Encerrar Atendimento                        \033[m")
    print("\033[1;31m╚════════════════════════════════════════════════════════════╝\033[m")
    if cartaoSUS not in data:
        print('\n❌ Não existe atendimento com esse cartão.\n')
        input('Pressione ENTER para voltar ao menu.')
    else:
        confirmar = inputConsistente('Deseja encerrar o atendimento? (S/N): ', 'cancelar')
        if confirmar == 'não':
            print('\n❌ Encerramento de atendimento cancelado com sucesso!')
        else:
            data.pop(cartaoSUS)
            print('\n✅ Atendimento encerrado com sucesso.')
        input('Pressione ENTER para voltar ao menu.')

def pesquisaAtendimento(cartaoSUS, data):
    clearScreen()
    print("\033[1;36m╔════════════════════════════════════════════════════════════╗\033[m")
    print("\033[1;36m              🔍 Pesquisa por Cartão SUS                      \033[m")
    print("\033[1;36m╚════════════════════════════════════════════════════════════╝\033[m")
    if cartaoSUS in data:
        paciente = data[cartaoSUS]
        print('\033[1;36m╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n')
        print(f'      🪪  \033[1;36m Cartão SUS: \033[m {cartaoSUS} \033[1;36m ‖ \033[m 🧍  \033[1;36m Nome: \033[m {paciente[0]} \033[1;36m ‖ \033[m 🆔  \033[1;36m CPF: \033[m {paciente[1]} \033[1;36m ‖ \033[m 🔢  \033[1;36m Idade: \033[m {paciente[2]} \033[1;36m ‖ \033[m ♂️♀️  \033[1;36m Sexo: \033[m {paciente[3]} \033[1;36m \n \033[m     🌡️  \033[1;36m Sintomas: \033[m {paciente[4]} \n      💳  \033[1;36m Convênio: \033[m {paciente[5]}\n')
        print('\033[1;36m╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')
    else:
        print(f'\n❌ Nenhum registro encontrado com o número de cartão do SUS: {cartaoSUS}.')
    input('\nPressione ENTER para continuar.')

def relatórioGeral(data):
    clearScreen()
    print("\033[1;35m╔════════════════════════════════════════════════════════════╗\033[m")
    print("\033[1;35m                     📋 Relatório Geral                       \033[m")
    print("\033[1;35m╚════════════════════════════════════════════════════════════╝\033[m")
    if not data:
        print('\n❌ Nenhum registro encontrado.')
    else:
        print('\n📋 Relatório Geral de Atendimentos:')
        i = 0
        print('\033[1;36m╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n')
        for cartaoSUS, paciente in data.items():
            print(f'      🪪  \033[1;36m Cartão SUS: \033[m {cartaoSUS} \033[1;36m ‖ \033[m 🧍  \033[1;36m Nome: \033[m {paciente[0]} \033[1;36m ‖ \033[m 🆔  \033[1;36m CPF: \033[m {paciente[1]} \033[1;36m ‖ \033[m 🔢  \033[1;36m Idade: \033[m {paciente[2]} \033[1;36m ‖ \033[m ♂️♀️  \033[1;36m Sexo: \033[m {paciente[3]} \033[1;36m \n \033[m     🌡️  \033[1;36m Sintomas: \033[m {paciente[4]} \n      💳  \033[1;36m Convênio: \033[m {paciente[5]}\n')
            i = i + 1
            if len(data.items()) > 1 and len(data.items()) > i :
                print('\033[1;36m╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣\n')
        print('\033[1;36m╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')
    input('\nPressione ENTER para continuar.')