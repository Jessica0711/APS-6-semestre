import tkinter as tk
from tkinter.filedialog import askopenfilename 

class TelaCadastro :
    
    def __init__(self, master =None):

        #Primeiro container da janela 
        self.primeiroContainer = tk.Frame(master)
        self.primeiroContainer ["bg"] = ("#BDECB6")
        self.primeiroContainer.pack()

        #Título
        self.titulo = tk.Label(self.primeiroContainer, text="Ministério do Meio Ambiente" )
        self.titulo ["font"] = ("Britannic Bold", "16")
        self.titulo ["bg"] = ("#BDECB6")
        self.titulo ["fg"] = ("#32471F")
        self.titulo.grid(rowspan = 2, pady=35)

        #Traçado abaixo do título
        self.barra = tk.Label (self.primeiroContainer, text= "_______________")
        self.barra ["font"] = ("Arial", "16", "bold")
        self.barra ["bg"] = ("#BDECB6")
        self.barra ["fg"] = ("#32471F")
        self.barra.grid(row=1, column = 0,rowspan=2)

    
        #Segundo container da janela 
        self.segundoContainer = tk.Frame(master)
        self.segundoContainer ["bg"] = ("#BDECB6")
        self.segundoContainer.pack()

        #Descrição
        self.descricao = tk.Label(self.segundoContainer)
        self.descricao ["text"] = ("Seja bem-vindo!")
        self.descricao ["fg"] = ("#5E8300")
        self.descricao ["font"] = ("Britannic Bold", "14")
        self.descricao ["bg"] = ("#BDECB6")
        self.descricao.grid(row=2,column=0)

        #Segundo container da janela 
        self.terceiroContainer = tk.Frame(master)
        self.terceiroContainer ["bg"] = ("#BDECB6")
        self.terceiroContainer.pack()

        #Descrição
        self.descricao = tk.Label(self.terceiroContainer)
        self.descricao ["text"] = ("Você está logado na nossa plataforma.")
        self.descricao ["fg"] = ("#5E8300")
        self.descricao ["font"] = ("Britannic Bold", "11")
        self.descricao ["bg"] = ("#BDECB6")
        self.descricao.grid(row=3,column=1, pady=5)

        #Quarto container da janela
        self.quartoContainer = tk.Frame(master)
        self.quartoContainer ["bg"] = ("#BDECB6")
        self.quartoContainer.pack(pady=40)

        #Nome 
        self.nome = tk.Label(self.quartoContainer)
        self.nome ["text"] = ("Nome:")
        self.nome ["fg"] = ("#32471F")
        self.nome ["font"] = ("Britannic Bold", "11")
        self.nome ["bg"] = ("#BDECB6")
        self.nome.grid(row=4,column=0)
        
        #Usuario
        self.nomeUsuario = tk.Label(self.quartoContainer)
        self.nomeUsuario ["text"] = ("Ex: Luiz Antonio")
        self.nomeUsuario ["fg"] = ("#808080")
        self.nomeUsuario ["font"] = ("Britannic Bold", "11", "italic")
        self.nomeUsuario ["bg"] = ("#BDECB6")
        self.nomeUsuario.grid(row=4,column=1)

        #Senha
        self.senha = tk.Label(self.quartoContainer)
        self.senha ["text"] = ("Senha:")
        self.senha["fg"] = ("#32471F")
        self.senha["font"] = ("Britannic Bold", "11")
        self.senha["bg"] = ("#BDECB6")
        self.senha.grid(row=5,column=0)
        
        #Senha do usuario
        self.senhaUsuario = tk.Label(self.quartoContainer)
        self.senhaUsuario ["text"] = ("Ex: 12345")
        self.senhaUsuario ["fg"] = ("#808080")
        self.senhaUsuario ["font"] = ("Britannic Bold", "11", "italic")
        self.senhaUsuario ["bg"] = ("#BDECB6")
        self.senhaUsuario.grid(row=5,column=1)

        #Nivel de acesso
        self.nivelAcesso = tk.Label(self.quartoContainer)
        self.nivelAcesso ["text"] = ("Nivel de acesso:")
        self.nivelAcesso["fg"] = ("#32471F")
        self.nivelAcesso["font"] = ("Britannic Bold", "11")
        self.nivelAcesso["bg"] = ("#BDECB6")
        self.nivelAcesso.grid(row=6,column=0)
        
        #Nivel de acesso do usuario
        self.nivelUsuario = tk.Label(self.quartoContainer)
        self.nivelUsuario ["text"] = ("Ex: 1")
        self.nivelUsuario ["fg"] = ("#808080")
        self.nivelUsuario ["font"] = ("Britannic Bold", "11", "italic")
        self.nivelUsuario ["bg"] = ("#BDECB6")
        self.nivelUsuario.grid(row=6,column=1)

        #Quinto container da janela
        self.quintoContainer = tk.Frame(master)
        self.quintoContainer ["bg"] = ("#BDECB6")
        self.quintoContainer.pack()

        #Botão Ver dados
        self.dados= tk.Button (self.quintoContainer, text = " Ver meus dados")
        self.dados ["bd"] = 0
        self.dados ["width"] = 15
        self.dados ["height"] = 1
        self.dados ["bg"] = ("#32471F")
        self.dados ["activebackground"] = ("#BDECB6")
        self.dados ["fg"] = ("white")
        self.dados ["font"] = ("Britannic Bold", "11")
        self.dados.grid(row =7, column=0, pady=30, padx=10)

        #Botão Sair
        self.sair = tk.Button (self.quintoContainer, text = "Sair")
        self.sair ["bd"] = 0
        self.sair ["width"] = 12
        self.sair ["height"] = 1
        self.sair ["bg"] = ("#BDECB6")
        self.sair ["activebackground"] = ("#BDECB6")
        self.sair ["fg"] = ("#32471F")
        self.sair ["font"] = ("Britannic Bold", "11")
        self.sair.grid(row=7,column = 1, pady=30)


        root.geometry("350x470")
        root ["bd"] = 10
        root["bg"] = ("#BDECB6")
        root.resizable(0,0)

root = tk.Tk()
TelaCadastro(root)
root.mainloop()