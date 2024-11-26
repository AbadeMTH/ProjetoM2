import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from functions import getDados, saveDados
from functionsInterfaceGrafica import inputConsistente

dadosLocal = {}

#Carregando dados do TXT e colocando dentro do programa
if len(getDados()) > 0:
    dadosLocal = getDados()

def RelatórioGeral(): #Função que manipula algumas coisas da interface e mostra os dados do programa em uma tabela por meio de uma treeview
    botaoEditar.configure(state='normal')
    botaoEsconderRelatorio.configure(state='normal')
    botaoEncerrar.configure(state='normal')
    treeview.delete(*treeview.get_children())
    treeview.place(relx=0.5, rely=0.4, anchor=N)
    instruçõesRolagem.place(relx=0.5, rely=0.65, anchor=CENTER)
    instruçõesEdição.place(relx=0.5, rely=0.68, anchor=CENTER)
    #Carrega dados na Treeview
    for chave,dados in dadosLocal.items(): #Looping que insere os dados na tabela   
        i=[chave,dados[0],dados[1],dados[2],dados[3],dados[4],dados[5]]
        treeview.insert('', END, values=i)

def AdicionarAtendimento(): #Função que manipula a interface e prepara para a adição do novo atendimento
    treeview.delete(*treeview.get_children())
    treeview.place_forget()
    
    #Desabilitando botões
    botaoRelatorio.configure(state='disabled')
    botaoEsconderRelatorio.configure(state='disabled')
    botaoSair.configure(state='disabled')
    botaoEncerrar.configure(state='disabled')
    botaoEditar.configure(state='disabled')
    botaoAdicionar.configure(state='disabled')
    titulo.place_forget()
    instruçõesEdição.place_forget()
    instruçõesRolagem.place_forget()

    #Colocando inputs na janela
    tituloFormulario.place(relx=0.5, rely=0.35, anchor=CENTER)

    lbl_cartaoSUS.place(relx=0.4, rely=0.39, anchor=CENTER)
    cartaoSUS.place(relx=0.4, rely=0.42, anchor=CENTER)

    lbl_nome.place(relx=0.5, rely=0.39, anchor=CENTER)
    nome.place(relx=0.5, rely=0.42, anchor=CENTER)

    lbl_cpf.place(relx=0.6, rely=0.39, anchor=CENTER)
    cpf.place(relx=0.6, rely=0.42, anchor=CENTER)

    lbl_idade.place(relx=0.4, rely=0.46, anchor=CENTER)
    idade.place(relx=0.4, rely=0.49, anchor=CENTER)

    lbl_sexo.place(relx=0.5, rely=0.46, anchor=CENTER)
    sexo.place(relx=0.5, rely=0.49, anchor=CENTER)

    lbl_sintomas.place(relx=0.6, rely=0.46, anchor=CENTER)
    sintomas.place(relx=0.6, rely=0.49, anchor=CENTER)

    lbl_convenio.place(relx=0.5, rely=0.53, anchor=CENTER)
    convenio.place(relx=0.5, rely=0.56, anchor=CENTER)

    botaoSalvar.place(relx=0.45, rely=0.61, anchor=CENTER)
    botaoVoltar.place(relx=0.55, rely=0.61, anchor=CENTER)

def SalvarAtendimento(): #Função que salva o novo atendimento feito pelo usuário
    #Reabilitando botões
    botaoRelatorio.configure(state='normal')
    botaoEsconderRelatorio.configure(state='normal')
    botaoSair.configure(state='normal')

    #Salvando dados
    CartaoSUS = inputConsistente(cartaoSUS.get(), 'int')
    Nome = inputConsistente(nome.get(),'str')
    Cpf = inputConsistente(cpf.get(), 'cpf')
    Idade = inputConsistente(idade.get(), 'idade')
    Sexo = inputConsistente(sexo.get(),'sexo')
    Sintomas = inputConsistente(sintomas.get(),'sintomas')
    Convenio = inputConsistente(convenio.get(),'str')
    if CartaoSUS == 'None' or Nome == 'None' or Cpf == 'None' or Idade == 'None' or Sexo == 'None' or Sintomas == 'None' or Convenio == 'None' :
        showinfo(title='Atenção', message='Algum dado está inválido')
    elif CartaoSUS in dadosLocal:
        showinfo(title='Atenção', message='O Cartão SUS digitado já existe!')
    else:
        dadosLocal[CartaoSUS] = [Nome, Cpf, Idade, Sexo, Sintomas, Convenio]

        #Apagando inputs e botão
        lbl_cartaoSUS.place_forget()
        cartaoSUS.place_forget()
        cartaoSUS.delete(0, END)
        lbl_nome.place_forget()
        nome.place_forget()
        nome.delete(0, END)
        lbl_cpf.place_forget()
        cpf.place_forget()
        cpf.delete(0, END)
        lbl_idade.place_forget()
        idade.place_forget()
        idade.delete(0, END)
        lbl_sexo.place_forget()
        sexo.place_forget()
        sexo.delete(0, END)
        lbl_sintomas.place_forget()
        sintomas.place_forget()
        sintomas.delete(0, END)
        lbl_convenio.place_forget()
        convenio.place_forget()
        convenio.delete(0, END)
        botaoSalvar.place_forget()
        botaoVoltar.place_forget()
        tituloFormulario.place_forget()
        titulo.place(relx=0.5, rely=0.35, anchor=CENTER) 
        botaoEsconderRelatorio.configure(state='disabled')
        botaoAdicionar.configure(state='normal')

        showinfo('Sucesso!', 'Atendimento adicionado com sucesso!')
        saveDados(dadosLocal)
    
def EditarAtendimento(): #Função que manipula a interface e prepara para a edição do atendimento existente
    global CartaoSUS_Alt
    global Nome_Alt
    global Cpf_Alt
    global Idade_Alt
    global Sexo_Alt
    global Sintomas_Alt
    global Convenio_Alt
    nome.delete(0, END)
    cpf.delete(0, END)
    idade.delete(0, END)
    sexo.delete(0, END)
    sintomas.delete(0, END)
    convenio.delete(0, END)
    if not treeview.focus():
        showinfo(title='ERRO', message='Selecione um item para Alteração')
        RelatórioGeral()
    else:
        instruçõesEdição.place_forget()
        instruçõesRolagem.place_forget()
        botaoRelatorio.configure(state='disabled')
        botaoEsconderRelatorio.configure(state='disabled')
        botaoAdicionar.configure(state='disabled')
        botaoEditar.configure(state='disabled')
        botaoEncerrar.configure(state='disabled')
        botaoSair.configure(state='disabled')
        # Coletando qual item está selecionado.
        item_selecionado = treeview.focus()
        rowid = treeview.item(item_selecionado)
        CartaoSUS_Alt = (rowid["values"][0])
        Nome_Alt = (rowid["values"][1])
        Cpf_Alt = (rowid["values"][2])
        Idade_Alt = (rowid["values"][3])
        Sexo_Alt = (rowid["values"][4])
        Sintomas_Alt = (rowid["values"][5])
        Convenio_Alt = (rowid["values"][6])
        
        treeview.place_forget()

        titulo.place_forget()
        tituloFormularioAlt.place(relx=0.5, rely=0.35, anchor=CENTER)

        lbl_nome.place(relx=0.4, rely=0.39, anchor=CENTER)
        nome.insert(0, Nome_Alt)
        nome.place(relx=0.4, rely=0.42, anchor=CENTER)

        lbl_cpf.place(relx=0.5, rely=0.39, anchor=CENTER)
        cpf.insert(0, Cpf_Alt)
        cpf.place(relx=0.5, rely=0.42, anchor=CENTER)

        lbl_idade.place(relx=0.6, rely=0.39, anchor=CENTER)
        idade.insert(0, Idade_Alt)
        idade.place(relx=0.6, rely=0.42, anchor=CENTER)

        lbl_sexo.place(relx=0.4, rely=0.46, anchor=CENTER)
        sexo.insert(0, Sexo_Alt)
        sexo.place(relx=0.4, rely=0.49, anchor=CENTER)

        lbl_sintomas.place(relx=0.5, rely=0.46, anchor=CENTER)
        sintomas.insert(0, Sintomas_Alt)
        sintomas.place(relx=0.5, rely=0.49, anchor=CENTER)

        lbl_convenio.place(relx=0.6, rely=0.46, anchor=CENTER)
        convenio.insert(0, Convenio_Alt)
        convenio.place(relx=0.6, rely=0.49, anchor=CENTER)

        botaoSalvarEdicao.place(relx=0.45, rely=0.54, anchor=CENTER)
        botaoVoltar.place(relx=0.55, rely=0.54, anchor=CENTER)

def SalvarEdição(): #Função que salva a edição do atendimento feita pelo usuário
    #Salvando dados
    Nome_Alt = inputConsistente(nome.get(),'str')
    Cpf_Alt = inputConsistente(cpf.get(), 'cpf')
    Idade_Alt = inputConsistente(idade.get(), 'idade')
    Sexo_Alt = inputConsistente(sexo.get(),'sexo')
    Sintomas_Alt = inputConsistente(sintomas.get(),'sintomas')
    Convenio_Alt = inputConsistente(convenio.get(),'str')
    if Nome_Alt == 'None' or Cpf_Alt == 'None' or Idade_Alt == 'None' or Sexo_Alt == 'None' or Sintomas_Alt == 'None' or Convenio_Alt == 'None' :
        showinfo(title='Atenção', message='Algum dado está inválido')
    else:
        selected_item = treeview.selection()[0]
        treeview.item(selected_item, values=(CartaoSUS_Alt, Nome_Alt, Cpf_Alt, Idade_Alt, Sexo_Alt, Sintomas_Alt, Convenio_Alt))
        dadosLocal[CartaoSUS_Alt] = [Nome_Alt, Cpf_Alt, Idade_Alt, Sexo_Alt, Sintomas_Alt, Convenio_Alt]
        showinfo(title='Atenção', message='Registro Alterado')
        treeview.delete(*treeview.get_children())
        treeview.forget()
        #Apagando inputs e botão
        lbl_cartaoSUS.place_forget()
        cartaoSUS.place_forget()
        cartaoSUS.delete(0, END)
        lbl_nome.place_forget()
        nome.place_forget()
        nome.delete(0, END)
        lbl_cpf.place_forget()
        cpf.place_forget()
        cpf.delete(0, END)
        lbl_idade.place_forget()
        idade.place_forget()
        idade.delete(0, END)
        lbl_sexo.place_forget()
        sexo.place_forget()
        sexo.delete(0, END)
        lbl_sintomas.place_forget()
        sintomas.place_forget()
        sintomas.delete(0, END)
        lbl_convenio.place_forget()
        convenio.place_forget()
        convenio.delete(0, END)
        botaoSalvarEdicao.place_forget()
        botaoVoltar.place_forget()
        botaoRelatorio.configure(state='normal')
        botaoAdicionar.configure(state='normal')
        botaoSair.configure(state='normal')

        RelatórioGeral()
        saveDados(dadosLocal)

def Voltar(): #Função que manipula toda interface para voltar ao estado inicial
    #Apagando tudo que não seja o menu
    treeview.delete(*treeview.get_children())
    treeview.place_forget()
    #Apagando inputs e botão
    lbl_cartaoSUS.place_forget()
    cartaoSUS.place_forget()
    cartaoSUS.delete(0, END)
    lbl_nome.place_forget()
    nome.place_forget()
    nome.delete(0, END)
    lbl_cpf.place_forget()
    cpf.place_forget()
    cpf.delete(0, END)
    lbl_idade.place_forget()
    idade.place_forget()
    idade.delete(0, END)
    lbl_sexo.place_forget()
    sexo.place_forget()
    sexo.delete(0, END)
    lbl_sintomas.place_forget()
    sintomas.place_forget()
    sintomas.delete(0, END)
    lbl_convenio.place_forget()
    convenio.place_forget()
    convenio.delete(0, END)
    botaoSalvar.place_forget()
    botaoVoltar.place_forget()
    botaoSalvarEdicao.place_forget()
    tituloFormulario.place_forget()
    tituloFormularioAlt.place_forget()
    instruçõesEdição.place_forget()
    instruçõesRolagem.place_forget()
    titulo.place(relx=0.5, rely=0.35, anchor=CENTER)
    botaoAdicionar.configure(state='normal')

    #Reabilitando botões
    botaoRelatorio.configure(state='normal')
    botaoSair.configure(state='normal')

def EncerrarAtendimento(): #Função que exclui o atendimento selecionado pelo usuário
    if not treeview.focus():
        showinfo(title='Atenção', message='Nenhum atendimento foi selecionado')
        return
    else:
        item_selecionado = treeview.focus()
        rowid = treeview.item(item_selecionado)
        cartaoSUS_Excl = (rowid["values"][0])
        resposta = askyesno(title='Confirmação', message='Certeza que deseja excluir esse atendimento?')
        if resposta:
            dadosLocal.pop(cartaoSUS_Excl)
            showinfo(title='Sucesso', message='Atencimento encerrado com sucesso!')
            RelatórioGeral()
            saveDados(dadosLocal)
        else:
            showinfo(title='Atenção', message='Atendimento não excluído')
def FecharRelatório(): #Função que esconde a tabela de dados
    treeview.delete(*treeview.get_children())
    treeview.place_forget()
    instruçõesEdição.place_forget()
    instruçõesRolagem.place_forget()
    botaoEditar.configure(state='disabled')
    botaoEncerrar.configure(state='disabled')
    botaoEsconderRelatorio.configure(state='disabled')

def Sair(): #Função que faz a saída do programa
    resposta = askyesno(title='Sair e Salvar', message='Deseja sair do programa e salvar?')
    if resposta:
        saveDados(dadosLocal)
        janela.destroy() #Destrói a janela

#Definições de temas
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Definição para a tela do programa
janela = customtkinter.CTk() #Criação da janela
janela.iconbitmap(default='icon.ico') #Troca do icone padrão para um ícone chamado icon
janela.title('Atendimento Prático de Saúde') #Troca do título do programa
janela.after(0, lambda:janela.state('zoomed')) #Aplicando a tela em tamanho máximo possísvel ao abrir   

#Definição da treeview (tabela) e suas colunas
columns=('Cartão SUS', 'Nome', 'CPF', 'Idade', 'Sexo', 'Sintomas', 'Convênio')
treeview = ttk.Treeview(janela, columns=columns, show="headings")
treeview.column('#1', width=80, anchor=CENTER)
treeview.column('#2', width=200, anchor=CENTER)
treeview.column('#3', width=100, anchor=CENTER)
treeview.column('#4', width=50, anchor=CENTER)
treeview.column('#5', width=80, anchor=CENTER)
treeview.column('#6', width=600, anchor=CENTER)
treeview.column('#7', width=100, anchor=CENTER)
treeview.heading('Cartão SUS', text='Cartão SUS')
treeview.heading('Nome', text='Nome')
treeview.heading('CPF', text='CPF')
treeview.heading('Idade', text='Idade')
treeview.heading('Sexo', text='Sexo')
treeview.heading('Sintomas', text='Sintomas')
treeview.heading('Convênio', text='Convênio')

#Titulo
titulo = customtkinter.CTkLabel(janela, text="Sistema de Atendimento Hospitalar", font=('',20)) #Criação do titulo
titulo.place(relx=0.5, rely=0.35, anchor=CENTER) #Inserindo o titulo na janela

#Botões
botaoRelatorio = customtkinter.CTkButton(janela, text="Relatório Geral", command=RelatórioGeral)
botaoRelatorio.place(relx=0.1, rely=0.35, anchor=NW)

botaoEsconderRelatorio = customtkinter.CTkButton(janela, text="Fechar Relatório", command=FecharRelatório)
botaoEsconderRelatorio.place(relx=0.1, rely=0.40)
botaoEsconderRelatorio.configure(state='disabled')

botaoAdicionar = customtkinter.CTkButton(janela, text="Adicionar Atendimento", command=AdicionarAtendimento)
botaoAdicionar.place(relx=0.1, rely=0.45, anchor=NW)

botaoEditar = customtkinter.CTkButton(janela, text="Editar Atendimento", command=EditarAtendimento)
botaoEditar.place(relx=0.1, rely=0.50, anchor=NW)
botaoEditar.configure(state='disabled')

botaoEncerrar = customtkinter.CTkButton(janela, text='Encerrar Atendimento', command=EncerrarAtendimento)
botaoEncerrar.place(relx=0.1, rely=0.55, anchor=NW)
botaoEncerrar.configure(state='disabled')

botaoSair = customtkinter.CTkButton(janela, text="Sair e Salvar", command=Sair)
botaoSair.place(relx=0.1, rely=0.6, anchor=NW)

botaoSalvar = customtkinter.CTkButton(janela, text="Salvar", command=SalvarAtendimento)

botaoSalvarEdicao = customtkinter.CTkButton(janela, text="Salvar Edição", command=SalvarEdição)

botaoVoltar = customtkinter.CTkButton(janela, text="Voltar", command=Voltar)

#Títulos
tituloFormulario = customtkinter.CTkLabel(janela, text="Formulário de Atendimento", font=('',20))

tituloFormularioAlt = customtkinter.CTkLabel(janela, text='Altere os dados do Atendimento', font=('',20))

instruçõesRolagem = customtkinter.CTkLabel(janela, text='Role a rodinha do mouse para navegar no relatório', font=('',14))
instruçõesEdição = customtkinter.CTkLabel(janela, text='Selecione um item para editar', font=('',14))

#Entrada de Dados
lbl_cartaoSUS = customtkinter.CTkLabel(janela, text="Cartão SUS")
cartaoSUS = customtkinter.CTkEntry(janela, placeholder_text="Cartão SUS")

lbl_nome = customtkinter.CTkLabel(janela, text="Nome")
nome = customtkinter.CTkEntry(janela, placeholder_text="Nome")

lbl_cpf = customtkinter.CTkLabel(janela, text="CPF")
cpf = customtkinter.CTkEntry(janela, placeholder_text="CPF")

lbl_idade = customtkinter.CTkLabel(janela, text="Idade")
idade = customtkinter.CTkEntry(janela, placeholder_text="Idade")

lbl_sexo = customtkinter.CTkLabel(janela, text="Sexo F/M")
sexo = customtkinter.CTkEntry(janela, placeholder_text="Sexo")

lbl_sintomas = customtkinter.CTkLabel(janela, text="Sintomas")
sintomas = customtkinter.CTkEntry(janela, placeholder_text="Sintomas")

lbl_convenio = customtkinter.CTkLabel(janela, text="Convênio")
convenio = customtkinter.CTkEntry(janela, placeholder_text="Convênio")

janela.mainloop() #Rodar o programa