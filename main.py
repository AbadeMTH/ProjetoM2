from functions import *

L1 = {}

clearScreen()

while True:
    menuOpt = inputConsistente('''
    Escolha uma opção:
    1 - Criar atendimento
    2 - Editar atendimento
    3 - Encerrar atendimento
    4 - Consultar atendimentos:
    5 - Pesquisa por cartão do SUS
                    ''', int)
    
    print(L1)

    if menuOpt not in [1, 2, 3, 4, 5]:
        clearScreen()
        print('\nOpção inválida. Tente novamente.\n')
    else:
        if menuOpt == 1:
            cartãoSUS = inputConsistente('Número do cartão SUS: ', int)
            criarAtendimento(cartãoSUS, L1)
        elif menuOpt == 2:
            cartãoSUS = inputConsistente('Digite o número do cartão SUS que deseja alterar: ', int)
            editarAtendimento(cartãoSUS, L1)
        elif menuOpt == 3:
            cartãoSUS = inputConsistente('Digite o número do cartão SUS que deseja remover: ', int)
            encerrarAtendimento(cartãoSUS, L1)
        elif menuOpt == 4:
            relatórioGeral(L1)
        else:
            cartãoSUS = inputConsistente('Número do cartão SUS: ', int)
            pesquisaAtendimento(cartãoSUS, L1)
            