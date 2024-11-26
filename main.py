#Software Básico - Eng. de SW e ADS Matutino - Prof. Luiz Carlos, Universidade de Mogi das Cruzes - UMC, Novembro de 2024
#Desenvolvedores: Wender Magela, Henrique Guido, Matheus Abade, Gabriel Santana, Vinicius Rodrigues

#Importando bibliotecas necessárias
from colorama import Fore, init
from functions import criarAtendimento, editarAtendimento, encerrarAtendimento, relatórioGeral, pesquisaAtendimento, inputConsistente, saveDados, getDados, clearScreen

#Inicializando biblioteca para cores
init(autoreset=True)

dadosLocal = {}

#Carregando dados do TXT e colocando dentro do programa
if len(getDados()) > 0:
    dadosLocal = getDados()
    
#Programa principal
while True:
    clearScreen()

    menuOpt = inputConsistente(f'''🩺  Sistema de Atendimento Hospitalar

    1 - 🆕 Criar atendimento
    2 - ✏️  Editar atendimento
    3 - ❌ Encerrar atendimento
    4 - 📋 Consultar atendimentos
    5 - 🔍 Pesquisa por cartão do SUS
    6 - 🚪 Sair e Salvar
    ''', 'int') 


    if menuOpt not in [1, 2, 3, 4, 5, 6]: #Usuário digitou opção inválida?
        clearScreen()
        print(Fore.RED + "⚠️ Opção inválida, Tente novamente.\n")
    else: #Digitou corretamente
        if menuOpt == 1: #Criar atendimento
            cartãoSUS = inputConsistente('🆔  Número do cartão SUS: ', 'int') 
            criarAtendimento(cartãoSUS, dadosLocal)
            saveDados(dadosLocal)
        
        elif menuOpt == 2: #Editar atendimento
            cartãoSUS = inputConsistente('✏️  Digite o número do cartão SUS que deseja alterar: ', 'int')
            editarAtendimento(cartãoSUS, dadosLocal)
            saveDados(dadosLocal)
        
        elif menuOpt == 3: #Encerrar atendimento
            cartãoSUS = inputConsistente('❌  Digite o número do cartão SUS que deseja remover: ', 'int')
            encerrarAtendimento(cartãoSUS, dadosLocal)
            relatórioGeral(dadosLocal)
            saveDados(dadosLocal)

        elif menuOpt == 4: #Consultar atendimentos
            relatórioGeral(dadosLocal)
        
        elif menuOpt == 5: #Pesquisa por cartão do SUS
            cartãoSUS = inputConsistente('🔍  Número do cartão SUS: ', 'int')
            pesquisaAtendimento(cartãoSUS, dadosLocal)
        
        else: #Sair e Salvar
            print(Fore.MAGENTA + "\n🙏  Obrigado por utilizar nosso aplicativo de atendimento hospitalar!")
            confirmar = inputConsistente('📝  Confirme para sair e salvar:\n       (S) - Sim  | (N) - Não: ', 'cancelar')
            if confirmar == 'sim':
                saveDados(dadosLocal)
                print(Fore.GREEN + '\n👋  Até mais! Cuide-se!')
                break
