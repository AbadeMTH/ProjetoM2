from functions import * #importação das funções criadas em outro arquivo

dadosLocal = {} #dicionário local

dados = getDados() #chamada de função que pega os dados armazenados no txt e retorna uma string, atribuímos essa string a uma variável

if len(dados) > 0: #caso exista dados no txt, formata a string para um dicionário
    dadosLocal = eval(dados) #eval transforma a string em um dicionário, atribuímos isso ao dicionário local

while True: #programa principal em looping
    clearScreen() #função para limpar a tela

    menuOpt = inputConsistente('''
    Escolha uma opção:
    1 - Criar atendimento
    2 - Editar atendimento
    3 - Encerrar atendimento
    4 - Consultar atendimentos:
    5 - Pesquisa por cartão do SUS
    6 - Sair
    ''', 'int') #criação de um menu utilizando o inputConsistente (função criada por nós), passando como parâmetro a string de pergunta e uma string do tipo do input
    
    #condicional para aplicação do menu
    if menuOpt not in [1, 2, 3, 4, 5, 6]: 
        clearScreen()
        print('\nOpção inválida. Tente novamente.\n')
    else:
        #caso usuário selecione Criar atendimento
        if menuOpt == 1: 
            #atribuição do inputConsistente a variável
            cartãoSUS = inputConsistente('Número do cartão SUS: ', 'int') 
            #chamada de função de criação de atendimento que tem como parâmetro o cartãoSUS como identificador e o dicionário local para salvamento local dos dados
            criarAtendimento(cartãoSUS, dadosLocal) 
        #caso usuário selecione Editar atendimento
        elif menuOpt == 2:
            #atribuição do inputConsistente a variável
            cartãoSUS = inputConsistente('Digite o número do cartão SUS que deseja alterar: ', 'int')
            #chamada de função de edição de atendimento que tem como parâmetro o cartãoSUS como identificador e o dicionário local para salvamento local dos dados
            editarAtendimento(cartãoSUS, dadosLocal)
        #caso usuário selecione Encerrar atendimento
        elif menuOpt == 3:
            #atribuição do inputConsistente a variável
            cartãoSUS = inputConsistente('Digite o número do cartão SUS que deseja remover: ', 'int')
            #chamada de função de remoção de atendimento que tem como parâmetro o cartãoSUS como identificador e o dicionário local para salvamento local dos dados
            encerrarAtendimento(cartãoSUS, dadosLocal)
        #caso usuário selecione Consultar atendimentos
        elif menuOpt == 4:
            #chamada de função de relatório geral que tem como parâmetro o dicionário local para listagem do mesmo
            relatórioGeral(dadosLocal)
        #caso usuário selecione Pesquisa por cartão do SUS
        elif menuOpt == 5:
            #atribuição do inputConsistente a variável
            cartãoSUS = inputConsistente('Número do cartão SUS: ', 'int')
            #chamada de função de pesquisa de atendimento que tem como parâmetro o cartãoSUS como identificador e o dicionário local para checagem e salvamento dos dados
            pesquisaAtendimento(cartãoSUS, dadosLocal)
        #caso o usuário seleciona Sair
        else:
            #chamada da função que salva os dados do dicionário local à um TXT, tem como parâmetro o dicionário local
            saveDados(dadosLocal)
            #fim do looping
            break