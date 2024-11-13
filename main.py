from colorama import Fore, init
from functions import criarAtendimento, editarAtendimento, encerrarAtendimento, relatórioGeral, pesquisaAtendimento, inputConsistente, saveDados, getDados, clearScreen

init(autoreset=True)

dadosLocal = {}

if len(getDados()) > 0:
    dadosLocal = getDados()
    
while True:
    clearScreen()

    menuOpt = inputConsistente(f'''🩺  Sistema de Atendimento Hospitalar

    1 - 🆕 Criar atendimento
    2 - ✏️  Editar atendimento
    3 - ❌ Encerrar atendimento
    4 - 📋 Consultar atendimentos
    5 - 🔍 Pesquisa por cartão do SUS
    6 - 🚪 Sair
    ''', 'int') 


    if menuOpt not in [1, 2, 3, 4, 5, 6]: 
        clearScreen()
        print(Fore.RED + "⚠️ Opção inválida, Tente novamente.\n")
    else:
        
        if menuOpt == 1: 
            cartãoSUS = inputConsistente('🆔  Número do cartão SUS: ', 'int') 
            criarAtendimento(cartãoSUS, dadosLocal)
        
        elif menuOpt == 2:
            cartãoSUS = inputConsistente('✏️  Digite o número do cartão SUS que deseja alterar: ', 'int')
            editarAtendimento(cartãoSUS, dadosLocal)
        
        elif menuOpt == 3:
            cartãoSUS = inputConsistente('❌  Digite o número do cartão SUS que deseja remover: ', 'int')
            encerrarAtendimento(cartãoSUS, dadosLocal)
            relatórioGeral(dadosLocal)

        elif menuOpt == 4:
            relatórioGeral(dadosLocal)
        
        elif menuOpt == 5:
            cartãoSUS = inputConsistente('🔍  Número do cartão SUS: ', 'int')
            pesquisaAtendimento(cartãoSUS, dadosLocal)
        
        else:
            print(Fore.MAGENTA + "\n🙏  Obrigado por utilizar nosso aplicativo de atendimento hospitalar!")
            confirmar = inputConsistente('📝  Confirme para sair:\n       (S) - Sim  | (N) - Não: ', 'cancelar')
            if confirmar == 'sim':
                saveDados(dadosLocal)
                print(Fore.GREEN + '\n👋  Até mais! Cuide-se!')
                break
