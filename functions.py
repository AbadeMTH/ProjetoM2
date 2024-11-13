#Software Básico - Eng. de SW e ADS Matutino - Prof. Luiz Carlos, Universidade de Mogi das Cruzes - UMC, Novembro de 2024
#Desenvolvedores: Wender Magela, Henrique Guido, Matheus Abade, Gabriel Santana, Vinicius Rodrigues

#Importando bibliotecas necessárias
import os
import re

#Inicializando lista e dicionário para manipulação dos dados
ListaDados = []
DicionárioPacientes = {}

#Função que limpa o terminal baseado no S.O
def clearScreen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

#Função que lê os dados, armazena em uma lista tirando caracteres de controle e separadores e joga esses dados para o dicionário tratando a tipagem
def getDados():
    try:
        with open("dados.txt", "r", encoding="utf-8") as dados:
            for linha in dados: #Para cada linha de registro do TXT
                ListaDados.append(linha.rstrip().split('|')) #rstrip() remove todos caracteres de controle a direita e split(',') separa os dados pela vírgula
            
            for dado in ListaDados: #Para cada lista de dados dentro da lista
                DicionárioPacientes[int(dado[0])] = [dado[1], int(dado[2]), int(dado[3]), dado[4], dado[5], dado[6]] #passando dados da lista para dicionário
            
            return DicionárioPacientes #Retorna o dicionário com os dados
    except FileNotFoundError: #Caso o TXT não existe retorna um dicionário vazio
        return {}

#Função que salva os dados no TXT
def saveDados(data):
    with open('dados.txt', 'w', encoding='utf8') as dadosTXT:
        for chave, dados in data.items(): #Para cada chave e dados do dicionário
            dadosTXT.write(f"{chave}|{dados[0]}|{dados[1]}|{dados[2]}|{dados[3]}|{dados[4]}|{dados[5]}\n") #Salvamos cada linha como string utilizando pipe como separador
    
#Função que consiste os inputs
def inputConsistente(perguntaInput, tipoDado):
    while True: #Looping para o usuário só avançar caso digite corretamente o que o input pede
        clearScreen()
        print("\033[1;34m╔════════════════════════════════════════════════════════════════╗\033[m")
        print(f"\033[1;34m   🏥 {perguntaInput}                                           \033[m")
        print("\033[1;34m╚════════════════════════════════════════════════════════════════╝\033[m")
        
        dadoTemp = input(f'\033[1;32m📝 Digite: \033[m')
        
        #Sequência de condições para cada tipo de input
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

#Função que cria o atendimento de um paciente
def criarAtendimento(cartaoSUS, data):
    clearScreen()
    print("\033[1;32m╔════════════════════════════════════════════════════════════╗ \033[m")
    print("\033[1;32m              🚑 Criar Novo Atendimento                           \033[m")
    print("\033[1;32m╚════════════════════════════════════════════════════════════╝ \033[m")
    if cartaoSUS in data: #Caso o cartaoSUS digitado pelo usuário ja exista
        print('\n❌ Já existe um atendimento com esse cartão.\n')
        input('Pressione ENTER para voltar ao menu.')
    else: #Caso o cartaoSUS digitado pelo usuário não exista
        nome = inputConsistente('Nome do paciente: ', 'str')
        cpf = inputConsistente('CPF do paciente: ', 'cpf')
        idade = inputConsistente('Idade do paciente: ', 'idade')
        sexo = inputConsistente('Sexo do paciente (M/F): ', 'sexo')
        sintomas = inputConsistente('Diga brevemente os sintomas do paciente (180 caracteres): ', 'sintomas')
        convenio = inputConsistente('Convênio do paciente: ', 'str')
        confirmar = inputConsistente('Deseja confirmar o atendimento? (S/N): ', 'cancelar')
        
        if confirmar == 'não': #Confirmação ou cancelamento
            print('\n❌ Atendimento cancelado com sucesso!')
        else:
            data[cartaoSUS] = [nome, cpf, idade, sexo, sintomas, convenio] #Adição dos dados digitados no dicionário
            print('\n✅ Atendimento criado com sucesso.')
        input('Pressione ENTER para voltar ao menu.')

#Função que altera um atendimento baseado no cartaoSUS
def editarAtendimento(cartaoSUS, data):
    clearScreen()
    print("\033[1;33m╔════════════════════════════════════════════════════════════╗\033[m")
    print("\033[1;33m              ✏️ Editar Atendimento                           \033[m")
    print("\033[1;33m╚════════════════════════════════════════════════════════════╝\033[m")

    if cartaoSUS not in data: #Caso o cartaoSUS digitado pelo usuário não exista
        print('\n❌ Não existe um atendimento com esse cartão.\n')
        input('Pressione ENTER para voltar ao menu.')
    else: #Caso o cartaoSUS digitado pelo usuário ja exista
        nome = inputConsistente('Altere o nome do paciente: ', 'str')
        cpf = inputConsistente('Altere o CPF do paciente: ', 'cpf')
        idade = inputConsistente('Altere a idade do paciente: ', 'idade')
        sexo = inputConsistente('Altere o sexo do paciente (M/F): ', 'sexo')
        sintomas = inputConsistente('Diga brevemente os sintomas do paciente (180 caracteres): ', 'sintomas')
        convenio = inputConsistente('Altere o convênio do paciente: ', 'str')
        confirmar = inputConsistente('Deseja confirmar a alteração? (S/N): ', 'cancelar')
        
        if confirmar == 'não': #Confirmação ou cancelamento
            print('\n❌ Alteração cancelada com sucesso!')
        else:
            data[cartaoSUS] = [nome, cpf, idade, sexo, sintomas, convenio] #Alteração dos dados digitados no dicionário
            print('\n✅ Atendimento alterado com sucesso.')
        input('Pressione ENTER para voltar ao menu.')

#Função que encerra um atendimento de paciente baseado no cartaoSUS
def encerrarAtendimento(cartaoSUS, data):
    clearScreen()
    print("\033[1;31m╔════════════════════════════════════════════════════════════╗\033[m")
    print("\033[1;31m               ⚠️ Encerrar Atendimento                        \033[m")
    print("\033[1;31m╚════════════════════════════════════════════════════════════╝\033[m")

    if cartaoSUS not in data: #Caso o cartaoSUS digitado pelo usuário não exista
        print('\n❌ Não existe atendimento com esse cartão.\n')
        input('Pressione ENTER para voltar ao menu.')
    else: #Caso o cartaoSUS digitado pelo usuário exista
        confirmar = inputConsistente('Deseja encerrar o atendimento? (S/N): ', 'cancelar')
        if confirmar == 'não': #Confirmação ou cancelamento
            print('\n❌ Encerramento de atendimento cancelado com sucesso!')
        else:
            data.pop(cartaoSUS) #Remoção dos dados do dicionário com base no cartaoSUS pelo método pop
            print('\n✅ Atendimento encerrado com sucesso.')
        input('Pressione ENTER para voltar ao menu.')

#Função que pesquisa um atendimento de paciente baseado no cartaoSUS
def pesquisaAtendimento(cartaoSUS, data):
    clearScreen()
    print("\033[1;36m╔════════════════════════════════════════════════════════════╗\033[m")
    print("\033[1;36m              🔍 Pesquisa por Cartão SUS                      \033[m")
    print("\033[1;36m╚════════════════════════════════════════════════════════════╝\033[m")

    if cartaoSUS in data: #Caso o cartaoSUS digitado pelo usuário exista
        paciente = data[cartaoSUS] #Atribuição dos dados relacionados ao cartaoSUS digitado à uma variável
        print('\033[1;36m╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n')
        print(f'      🪪  \033[1;36m Cartão SUS: \033[m {cartaoSUS} \033[1;36m ‖ \033[m 🧍  \033[1;36m Nome: \033[m {paciente[0]} \033[1;36m ‖ \033[m 🆔  \033[1;36m CPF: \033[m {paciente[1]} \033[1;36m ‖ \033[m 🔢  \033[1;36m Idade: \033[m {paciente[2]} \033[1;36m ‖ \033[m ♂️♀️  \033[1;36m Sexo: \033[m {paciente[3]} \033[1;36m \n \033[m     🌡️  \033[1;36m Sintomas: \033[m {paciente[4]} \n      💳  \033[1;36m Convênio: \033[m {paciente[5]}\n')
        print('\033[1;36m╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')
    else: #Caso o cartaoSUS digitado pelo usuário não exista
        print(f'\n❌ Nenhum registro encontrado com o número de cartão do SUS: {cartaoSUS}.')
    input('\nPressione ENTER para continuar.')

#Função que mostra todos os registros existentes
def relatórioGeral(data):
    clearScreen()
    print("\033[1;35m╔════════════════════════════════════════════════════════════╗\033[m")
    print("\033[1;35m                     📋 Relatório Geral                       \033[m")
    print("\033[1;35m╚════════════════════════════════════════════════════════════╝\033[m")

    if not data: #Caso não exista nenhum registro
        print('\n❌ Nenhum registro encontrado.')
    else: #Caso exista registros
        print('\n📋 Relatório Geral de Atendimentos:')
        i = 0 #Criação de uma variável para controle de estilização caso haja mais de 1 registro
        print('\033[1;36m╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗\n')
        for cartaoSUS, paciente in data.items(): #Para cada cartaoSUS e dados do paciente do dicionário
            print(f'      🪪  \033[1;36m Cartão SUS: \033[m {cartaoSUS} \033[1;36m ‖ \033[m 🧍  \033[1;36m Nome: \033[m {paciente[0]} \033[1;36m ‖ \033[m 🆔  \033[1;36m CPF: \033[m {paciente[1]} \033[1;36m ‖ \033[m 🔢  \033[1;36m Idade: \033[m {paciente[2]} \033[1;36m ‖ \033[m ♂️♀️  \033[1;36m Sexo: \033[m {paciente[3]} \033[1;36m \n \033[m     🌡️  \033[1;36m Sintomas: \033[m {paciente[4]} \n      💳  \033[1;36m Convênio: \033[m {paciente[5]}\n')
            i = i + 1 #Somamos i + 1 para controle de separação dos registros caso haja mais de 1 registro
            if len(data.items()) > 1 and len(data.items()) > i : #Condição que controla se deve ou não adicionar uma linha de separação entre registros
                print('\033[1;36m╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣\n')
        print('\033[1;36m╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝')
    input('\nPressione ENTER para continuar.')