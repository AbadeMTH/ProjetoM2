import re #importação da biblioteca para utilização de regex
import os #importação da biblioteca para limpar o terminal

def clearScreen(): #função que limpa o terminal baseado no sistema operacional
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

#função que pega os dados do TXT
def getDados(): 
    #abre o arquivo TXT como uma variável dadosTXT
    with open('dados.txt', encoding='utf8') as dadosTXT: 
        #atribui o resultado do método read do dadosTXT, transformado em string à variável data
        data = str(dadosTXT.read()) 
        #retorna a string de dados
        return data 

#função que salva os dados salvos localmente no TXT
def saveDados(data): 
    #abre o arquivo TXT como uma variável dadosTXT
    with open('dados.txt', 'w', encoding='utf8') as dadosTXT:
        #salva o conteúdo do dicionário passado por parâmetro, transformado em string no arquivo TXT 
        dadosTXT.write(str(data))

#função que trata os inputs com regex de acordo com o tipo especificado e recebendo a string para a pergunta
def inputConsistente(perguntaInput, tipoDado):
    #criação de uma variável para controle do looping e atribuição do dado tratado
    dado = ''
    #looping enquanto o dado for vazio
    while dado == '':
        #chamada da função que limpa o terminal
        clearScreen()
        #se o tipoDado especificado na chamada da função for 'str'
        if tipoDado == 'str':
            #passamos um input de string para variável dadoTemp (dado temporário), com a perguntaInput passada por parâmetro
            dadoTemp = input(f'\n{perguntaInput}')
            #verificação se o usuário escreveu apenas letras sem espaço no início e no final da string
            if re.match(r'^[A-Za-z]+( [A-Za-z]+)*$', dadoTemp):
                #caso o usuário escreveu corretamente atribui o dado temporário para a variável dado
                dado = dadoTemp
                #retorna dado, encerrando o looping
                return dado
            #caso usuário digitou errado
            else:
                #chamada da função que limpa o terminal
                clearScreen()
                print('\nDigite um texto válido.\n')
                input('Pressione ENTER para digitar novamente.')
                #atribui uma string vazia para retornar o looping
                dado = ''
        #se o tipoDado especificado na chamada da função for 'sexo'
        elif tipoDado == 'sexo':
            #passamos um input de string para variável dadoTemp (dado temporário), com a perguntaInput passada por parâmetro
            dadoTemp = input(f'\n{perguntaInput}')
            #verificação se o usuário escreveu apenas 1 letra, sendo ela m ou f maiúsculo ou minúsculo
            if len(dadoTemp) == 1 and dadoTemp in ['m', 'M', 'f', 'F'] :
                #caso o usuário escreveu corretamente atribui o dado temporário para a variável dado
                dado = dadoTemp
                #retorna dado, encerrando o looping
                return dado
            #caso usuário digitou errado
            else:
                #chamada da função que limpa o terminal
                clearScreen()
                print('\nDigite um texto válido.\n')
                input('Pressione ENTER para digitar novamente.')
                #atribui uma string vazia para retornar o looping
                dado = ''
        #se o tipoDado especificado na chamada da função for 'int'
        elif tipoDado == 'int':
            #passamos um input de string para variável dadoTemp (dado temporário), com a perguntaInput passada por parâmetro
            dadoTemp = input(f'\n{perguntaInput}')
            #verificação se o usuário digitou apenas números
            if re.match(r'^\d+$', dadoTemp):
                #caso o usuário escreveu corretamente atribui o dado temporário para a variável dado como um número inteiro
                dado = int(dadoTemp)
                #retorna dado, encerrando o looping
                return dado
            #caso usuário digitou errado
            else:
                #chamada da função que limpa o terminal
                clearScreen()
                print('\nDigite um valor válido.')
                input('Pressione ENTER para digitar novamente.')
                #atribui uma string vazia para retornar o looping
                dado = ''
        #se o tipoDado especificado na chamada da função for 'cpf'
        elif tipoDado == 'cpf':
            #passamos um input de string para variável dadoTemp (dado temporário), com a perguntaInput passada por parâmetro
            dadoTemp = input(f'\n{perguntaInput}')
            #verificação se o usuário digitou apenas número e se o tamanho do cpf digitado é válido (cpf tem 11 dígitos)
            if re.match(r'^\d+$', dadoTemp) and len(dadoTemp) == 11:
                #caso o usuário escreveu corretamente atribui o dado temporário para a variável dado como um número inteiro
                dado = int(dadoTemp)
                #retorna dado, encerrando o looping
                return dado
            #caso usuário digitou errado
            else:
                #chamada da função que limpa o terminal
                clearScreen()
                print('\nDigite um valor válido.')
                input('Pressione ENTER para digitar novamente.')
                #atribui uma string vazia para retornar o looping
                dado = ''
        #se o tipoDado especificado na chamada da função for 'idade'
        elif tipoDado == 'idade':
            #passamos um input de string para variável dadoTemp (dado temporário), com a perguntaInput passada por parâmetro
            dadoTemp = input(f'\n{perguntaInput}')
            #verificação se o usuário digitou apenas números e se digitou um número de 1 a 3 dígitos (idade pode ser 9 anos, 17 anos, 101 anos por exemplo)
            if re.match(r'^\d+$', dadoTemp) and len(dadoTemp) > 0 and len(dadoTemp) <= 3:
                #caso o usuário escreveu corretamente atribui o dado temporário para a variável dado como um número inteiro
                dado = int(dadoTemp)
                #retorna dado, encerrando o looping
                return dado
            #caso usuário digitou errado
            else:
                #chamada da função que limpa o terminal
                clearScreen()
                print('\nDigite um valor válido.')
                input('Pressione ENTER para digitar novamente.')
                #atribui uma string vazia para retornar o looping
                dado = ''
                #se o tipoDado especificado na chamada da função for 'float'
        elif tipoDado == 'float':
            #passamos um input de string para variável dadoTemp (dado temporário), com a perguntaInput passada por parâmetro
            dadoTemp = input(f'\n{perguntaInput}')
            #verificação se o usuário digitou apenas números reais
            if re.match(r'^\d+(\.\d+)?$', dadoTemp):
                #caso o usuário escreveu corretamente atribui o dado temporário para a variável dado como um número real
                dado = float(dadoTemp)
                #retorna dado, encerrando o looping
                return dado
            #caso usuário digitou errado
            else:
                #chamada da função que limpa o terminal
                clearScreen()
                print('\nDigite um valor válido.')
                input('Pressione ENTER para digitar novamente.')
                #atribui uma string vazia para retornar o looping
                dado = ''

#função que cria um atendimento baseado no cartãoSUS passado como parâmetro e adiciona no dicionário, salvando localmente
def criarAtendimento(cartãoSUS, data):
    #chamada da função que limpa o terminal
    clearScreen()
    #se o cartãoSUS digitado pelo usuário já existir
    if cartãoSUS in data:
        #chamada da função que limpa o terminal
        clearScreen()
        #mensagem que o cartãoSUS digitado ja existe
        print('\nJá existe um atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    #caso não exista ainda pergunta os dados e adiciona no dicionário localmente
    else:
        #inputs utilizando a função de inputConsistente para tratar os dados especificando a pergunta e o tipo do input como parâmetros
        nm = inputConsistente('Nome do paciente: ', 'str')
        cpf = inputConsistente('CPF do paciente: ', 'cpf')
        idade = inputConsistente('Idade do paciente: ', 'idade')
        sexo = inputConsistente('Sexo do paciente (M/F): ', 'sexo')
        sintomas = inputConsistente('Sintomas do paciente: ', 'str')
        convênio = inputConsistente('Convênio do paciente: ', 'str')

        #adicionando os dados no dicionário local com o método update
        data.update({cartãoSUS: [nm, cpf, idade, sexo, sintomas, convênio]})
        print(f'\nAtendimento criado com sucesso.\n')
        input('Pressione ENTER para voltar ao menu')

#função que altera um atendimento baseado no cartãoSUS passado como parâmetro e adiciona o registro alterado no dicionário, salvando localmente
def editarAtendimento(cartãoSUS,data):
    #chamada da função que limpa o terminal
    clearScreen()
    #se o cartãoSUS digitado pelo usuário NÃO existir
    if cartãoSUS not in data:
        #mensagem de aviso que não existe o cartão digitado
        print('\nNão existe um atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    #caso usuário digitou um cartãoSUS existente
    else:
        print(f'\nDigite em seguida a alteração dos dados relacionados ao cartão do SUS de número: {cartãoSUS}')

        #inputs utilizando a função de inputConsistente para tratar os dados especificando a pergunta e o tipo do input como parâmetros
        nm = inputConsistente('Nome do paciente: ', 'str')
        cpf = inputConsistente('CPF do paciente: ', 'cpf')
        idade = inputConsistente('Idade do paciente: ', 'idade')
        sexo = inputConsistente('Sexo do paciente (M/F): ', 'sexo')
        sintomas = inputConsistente('Sintomas do paciente: ', 'str')
        convênio = inputConsistente('Convênio do paciente: ', 'str')

        #atualizando os dados no dicionário local com o método update 
        data.update({cartãoSUS: [nm, cpf, idade, sexo, sintomas, convênio]  })
        print(f'\nAtendimento alterado com sucesso.\n')
        input('Pressione ENTER para voltar ao menu')

#função que remove um atendimento baseado no cartãoSUS passado como parâmetro
def encerrarAtendimento(cartãoSUS, data):
    #chamada da função que limpa o terminal
    clearScreen()
    #se o cartãoSUS digitado pelo usuário NÃO existir
    if cartãoSUS not in data:
        print('\nNão existe atendimento com esse cartão.\n')
        input('Digite ENTER para voltar ao menu.')
    #caso usuário digitou um cartãoSUS existente
    else:
        #removendo o registro do dicionário local baseado no cartãoSUS digitado pelo usuário
        data.pop(cartãoSUS)
        print(f'\nAtendimento encerrado com sucesso.\n')
        input('Pressione ENTER para voltar ao menu')

#função que pesquisa um atendimento com base no cartãoSUS digitado pelo usuário
def pesquisaAtendimento(cartãoSUS, data):
    #chamada da função que limpa o terminal
    clearScreen()
    print('\nRegistro(s) de Cartão do SUS de acordo com o nome informado:\n')
    
    #se o cartãoSUS existir no dicionário local, mostra o registro
    if cartãoSUS in data:
        print(f'\nCartão do SUS: {cartãoSUS} | Nome: {data[cartãoSUS][0]} | CPF: {data[cartãoSUS][1]} | Idade: {data[cartãoSUS][2]} | Sexo: {data[cartãoSUS][3]} | Sintomas: {data[cartãoSUS][4]} | Convênio: {data[cartãoSUS][5]}\n')
    #caso usuário digitou um cartãoSUS inexistente no dicionário local
    else:
        #mensagem de aviso que não existe registro com esse número de cartão
        print(f'\nNenhum registro encontrado com o número de cartão do SUS>: {cartãoSUS}.')
    
    #para voltar ao menu nas 2 situações
    input('\nDigite ENTER para continuar.')

#função que mostra TODOS os atendimentos existentes no dicionário local
def relatórioGeral(data):
    #chamada da função que limpa o terminal
    clearScreen()
    #se o tamanho do dicionário local for 0 (não existe nada armazenado)
    if len(data) == 0:
        #mensagem de aviso que não existem atendimentos
        print('\nNenhum registro encontrado.')
        input('\nPressione ENTER para voltar ao menu.')
    #caso existam atendimentos
    else:
        #para cara chave primária (cartãoSUS), registre cada um de seus dados na variável dados com o método items()
        for cartãoSUS, dados in data.items():
            #registro com chave primária e dados
            print(f'\nCartão do SUS: {cartãoSUS} | Nome: {dados[0]} | CPF: {dados[1]} | Idade: {dados[2]} | Sexo: {dados[3]} | Sintomas: {dados[4]} | Convênio: {dados[5]}\n')
        
        input('\nPressione ENTER para voltar ao menu.')
