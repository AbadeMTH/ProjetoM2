import customtkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from functions import getDados, saveDados
from functionsInterfaceGrafica import inputConsistente

dadosLocal = {}

#Carregando dados do TXT e colocando dentro do programa
if len(getDados()) > 0:
    dadosLocal = getDados()

def RelatórioGeral():
    botaoEditar.configure(state='normal')
    treeview.delete(*treeview.get_children())
    treeview.pack(padx= 10, pady= 10) 
    #Carrega dados na Treview
    for chave,dados in dadosLocal.items():        
        i=[chave,dados[0],dados[1],dados[2],dados[3],dados[4],dados[5]]
        treeview.insert('', END, values=i)

def AdicionarAtendimento():
    treeview.delete(*treeview.get_children())
    treeview.forget()
    botaoEditar.configure(state='disabled')

    #Desabilitando botões
    botaoRelatorio.configure(state='disabled')
    botaoEsconderRelatorio.configure(state='disabled')
    botaoSair.configure(state='disabled')

    #Colocando inputs na janela
    lbl_cartaoSUS.pack(padx= 10, pady= 2)
    cartaoSUS.pack(padx= 10, pady= 2)

    lbl_nome.pack(padx= 10, pady= 2)
    nome.pack(padx= 10, pady= 2)

    lbl_cpf.pack(padx= 10, pady= 2)
    cpf.pack(padx= 10, pady =2)

    lbl_idade.pack(padx= 10, pady= 2)
    idade.pack(padx= 10, pady= 2)

    lbl_sexo.pack(padx= 10, pady= 2)
    sexo.pack(padx= 10, pady= 2)

    lbl_sintomas.pack(padx= 10, pady= 2)
    sintomas.pack(padx= 10, pady= 2)

    lbl_convenio.pack(padx= 10, pady= 2)
    convenio.pack(padx= 10, pady= 2)

    botaoSalvar.pack(padx= 10, pady= 2,)
    botaoVoltar.pack(padx= 10, pady= 2)

def SalvarAtendimento():
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
    else:
        dadosLocal[CartaoSUS] = [Nome, Cpf, Idade, Sexo, Sintomas, Convenio]

        #Apagando inputs e botão
        lbl_cartaoSUS.forget()
        cartaoSUS.forget()
        cartaoSUS.delete(0, END)
        lbl_nome.forget()
        nome.forget()
        nome.delete(0, END)
        lbl_cpf.forget()
        cpf.forget()
        cpf.delete(0, END)
        lbl_idade.forget()
        idade.forget()
        idade.delete(0, END)
        lbl_sexo.forget()
        sexo.forget()
        sexo.delete(0, END)
        lbl_sintomas.forget()
        sintomas.forget()
        sintomas.delete(0, END)
        lbl_convenio.forget()
        convenio.forget()
        convenio.delete(0, END)
        botaoSalvar.forget()
        botaoVoltar.forget()
    
def EditarAtendimento():
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
    else:
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

        lbl_nome.pack(padx= 10, pady= 2)
        nome.insert(0, Nome_Alt)
        nome.pack(padx= 10, pady= 2)

        lbl_cpf.pack(padx= 10, pady= 2)
        cpf.insert(0, Cpf_Alt)
        cpf.pack(padx= 10, pady =2)

        lbl_idade.pack(padx= 10, pady= 2)
        idade.insert(0, Idade_Alt)
        idade.pack(padx= 10, pady= 2)

        lbl_sexo.pack(padx= 10, pady= 2)
        sexo.insert(0, Sexo_Alt)
        sexo.pack(padx= 10, pady= 2)

        lbl_sintomas.pack(padx= 10, pady= 2)
        sintomas.insert(0, Sintomas_Alt)
        sintomas.pack(padx= 10, pady= 2)

        lbl_convenio.pack(padx= 10, pady= 2)
        convenio.insert(0, Convenio_Alt)
        convenio.pack(padx= 10, pady= 2)

        botaoSalvarEdicao.pack(padx=10, pady= 2)
        botaoVoltar.pack(padx=10, pady= 2)

def SalvarEdição():
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
        lbl_cartaoSUS.forget()
        cartaoSUS.forget()
        cartaoSUS.delete(0, END)
        lbl_nome.forget()
        nome.forget()
        nome.delete(0, END)
        lbl_cpf.forget()
        cpf.forget()
        cpf.delete(0, END)
        lbl_idade.forget()
        idade.forget()
        idade.delete(0, END)
        lbl_sexo.forget()
        sexo.forget()
        sexo.delete(0, END)
        lbl_sintomas.forget()
        sintomas.forget()
        sintomas.delete(0, END)
        lbl_convenio.forget()
        convenio.forget()
        convenio.delete(0, END)
        botaoSalvar.forget()
        botaoVoltar.forget()

def Voltar():
    #Apagando tudo que não seja o menu
    treeview.delete(*treeview.get_children())
    treeview.forget()
    #Apagando inputs e botão
    lbl_cartaoSUS.forget()
    cartaoSUS.forget()
    cartaoSUS.delete(0, END)
    lbl_nome.forget()
    nome.forget()
    nome.delete(0, END)
    lbl_cpf.forget()
    cpf.forget()
    cpf.delete(0, END)
    lbl_idade.forget()
    idade.forget()
    idade.delete(0, END)
    lbl_sexo.forget()
    sexo.forget()
    sexo.delete(0, END)
    lbl_sintomas.forget()
    sintomas.forget()
    sintomas.delete(0, END)
    lbl_convenio.forget()
    convenio.forget()
    convenio.delete(0, END)
    botaoSalvar.forget()
    botaoVoltar.forget()
    botaoSalvarEdicao.forget()

    #Reabilitando botões
    botaoRelatorio.configure(state='normal')
    botaoEsconderRelatorio.configure(state='normal')
    botaoSair.configure(state='normal')
def FecharRelatório():
    treeview.delete(*treeview.get_children())
    treeview.forget()
    botaoEditar.configure(state='disabled')

def Sair():
    saveDados(dadosLocal)
    janela.destroy() #Destrói a janela

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk() #Criação da janela
janela.geometry("500x300") #Definição do tamanho inicial

columns=('Cartão SUS', 'Nome', 'CPF', 'Idade', 'Sexo', 'Sintomas', 'Convênio')
treeview = ttk.Treeview(janela, columns=columns, show="headings")
treeview.column('#1', width=100)
treeview.column('#2', width=200)
treeview.column('#3', width=200)
treeview.column('#4', width=100)
treeview.column('#5', width=100)
treeview.column('#6', width=100)
treeview.column('#7', width=100)
treeview.heading('Cartão SUS', text='Cartão SUS')
treeview.heading('Nome', text='Nome')
treeview.heading('CPF', text='CPF')
treeview.heading('Idade', text='Idade')
treeview.heading('Sexo', text='Sexo')
treeview.heading('Sintomas', text='Sintomas')
treeview.heading('Convênio', text='Convênio')

#Titulo
titulo = customtkinter.CTkLabel(janela, text="Sistema de Atendimento Hospitalar") #Criação do titulo
titulo.pack(padx = 10, pady = 10) #Inserindo o titulo na janela

#Botões
botaoRelatorio = customtkinter.CTkButton(janela, text="Relatório Geral", command=RelatórioGeral)
botaoRelatorio.place(x=10, y=10)

botaoAdicionar = customtkinter.CTkButton(janela, text="Adicionar Atendimento", command=AdicionarAtendimento)
botaoAdicionar.place(x=10, y=50)

botaoEditar = customtkinter.CTkButton(janela, text="Editar Atendimento", command=EditarAtendimento)
botaoEditar.place(x=10, y=90)
botaoEditar.configure(state='disabled')

botaoEsconderRelatorio = customtkinter.CTkButton(janela, text="Fechar Relatório", command=FecharRelatório)
botaoEsconderRelatorio.place(x=10, y=130)

botaoSair = customtkinter.CTkButton(janela, text="Sair", command=Sair)
botaoSair.place(x=10, y=170)

botaoSalvar = customtkinter.CTkButton(janela, text="Salvar", command=SalvarAtendimento)

botaoSalvarEdicao = customtkinter.CTkButton(janela, text="Salvar Edição", command=SalvarEdição)

botaoVoltar = customtkinter.CTkButton(janela, text="Voltar", command=Voltar)

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

janela.mainloop() #Rodar a janela