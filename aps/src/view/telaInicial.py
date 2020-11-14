import tkinter as tk
from tkinter import messagebox
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
        self.barra ["font"] = ("Arial", "14", "bold")
        self.barra ["bg"] = ("#BDECB6")
        self.barra ["fg"] = ("#32471F")
        self.barra.grid(row=1, column = 0,rowspan=2, pady=57)

    
        #Segundo container da janela 
        self.segundoContainer = tk.Frame(master)
        self.segundoContainer ["bg"] = ("#BDECB6")
        self.segundoContainer.pack()

        #Descrição
        self.descricao = tk.Label(self.segundoContainer)
        self.descricao ["text"] = ("Seja bem-vindo, entre com seus dados: ")
        self.descricao ["fg"] = ("#5E8300")
        self.descricao ["font"] = ("Britannic Bold", "11")
        self.descricao ["bg"] = ("#BDECB6")
        self.descricao.grid(row=2,column=1, pady=10)

        #Terceiro container da janela 
        self.terceiroContainer = tk.Frame(master)
        self.terceiroContainer ["bg"] = ("#BDECB6")
        self.terceiroContainer.pack()

        #Login e configurações
        self.login = tk.Label (self.terceiroContainer)
        self.login ["text"] = ("Login:")
        self.login ["fg"] = ("#32471F")
        self.login ["font"] = ("Britannic Bold", "11")
        self.login ["bg"] = ("#BDECB6")
        self.login.grid(row=3,column=1)

        #Campo do login
        self.campoLogin = tk.Entry(self.terceiroContainer)
        self.campoLogin["width"] = 30
        self.campoLogin ["font"] = ("Arial", "9")
        self.campoLogin.grid(row=3,column=2, padx=5)

        #Quarto container da janela 
        self.quartoContainer = tk.Frame(master)
        self.quartoContainer ["bg"] = ("#BDECB6")
        self.quartoContainer.pack()

        #Senha e configurações
        self.senha = tk.Label (self.quartoContainer)
        self.senha ["text"] = ("Senha:")
        self.senha ["fg"] = ("#32471F")
        self.senha ["font"] = ("Britannic Bold", "11")
        self.senha ["bg"] = ("#BDECB6")
        self.senha.grid(row=4,column=1, pady=5)

        #Campo do senha
        self.campoSenha = tk.Entry(self.quartoContainer)
        self.campoSenha["width"] = 30
        self.campoSenha ["font"] = ("Arial", "9")
        self.campoSenha["show"] = "*"
        self.campoSenha.grid(row=4,column=2, padx=5, pady=5)
        
        #Quinta container da janela 
        self.quintoContainer = tk.Frame(master)
        self.quintoContainer ["bg"] = ("#BDECB6")
        self.quintoContainer.pack(pady=1)

        #Divisor 
        self.senha = tk.Label (self.quintoContainer)
        self.senha ["text"] = ("ou")
        self.senha ["fg"] = ("#32471F")
        self.senha ["font"] = ("Britannic Bold", "9")
        self.senha ["bg"] = ("#BDECB6")
        self.senha.grid(row=5,column=1)

        #Sexto container da janela 
        self.sextoContainer = tk.Frame(master)
        self.sextoContainer ["bg"] = ("#BDECB6")
        self.sextoContainer.pack(pady=1)

        #Biometria
        self.biometria = tk.Label(self.sextoContainer)
        self.biometria ["text"] = ("Digital:")
        self.biometria["fg"] = ("#32471F")
        self.biometria["font"] = ("Britannic Bold", "11")
        self.biometria["bg"] = ("#BDECB6")
        self.biometria.grid(row=6,column=1)

        #Botão da biometria
        self.campoBiometria = tk.Button(self.sextoContainer)
        self.campoBiometria ["text"] = ("Clique aqui e insira sua digital.")
        self.campoBiometria["width"] = 29
        self.campoBiometria ["command"]= self.abrirArquivo
        self.campoBiometria ["bd"] = 0
        self.campoBiometria ["activebackground"] = ("#BDECB6")
        self.campoBiometria["font"] = ("calibri", "10", "bold")
        self.campoBiometria["fg"] = ("#5E8300")
        self.campoBiometria["bg"] = ("#BDECB6")
        self.campoBiometria.grid(row=6,column=2)

        #Setimo container da janela 
        self.setimoContainer = tk.Frame(master)
        self.setimoContainer ["bg"] = ("#BDECB6")
        self.setimoContainer.pack(pady=65)

        #Botão Cadastrar
        self.cadastrar = tk.Button (self.setimoContainer, text = "Entrar")
        self.cadastrar ["bd"] = 0
        self.cadastrar ["width"] = 10
        self.cadastrar ["height"] = 1
        self.cadastrar ["bg"] = ("#5E8300")
        self.cadastrar ["activebackground"] = ("#BDECB6")
        self.cadastrar ["fg"] = ("white")
        self.cadastrar ["font"] = ("Britannic Bold", "12")
        self.cadastrar.grid(row =7, column=0)

        #Botão Voltar
        self.voltar = tk.Button(self.setimoContainer, text = "  ou   Cadastrar")
        self.voltar ["bd"] = 0
        self.voltar ["width"] = 12
        self.voltar ["height"] = 1
        self.voltar ["bg"] = ("#BDECB6")
        self.voltar ["activebackground"] = ("#BDECB6")
        self.voltar ["fg"] = ("#32471F")
        self.voltar ["font"] = ("Britannic Bold", "12")
        self.voltar.grid(row=7,column = 1, columnspan = 1)

    

        root.geometry("350x470")
        root ["bd"] = 10
        root["bg"] = ("#BDECB6")
        root.resizable(0,0)

    
    #Função para abrir arquivo
    def abrirArquivo (self):
      self.digital = askopenfilename(initialfile="/Desktop", title= "Selecione à sua digital", filetype=(("Arquivo de imagem", ".jpeg"),("Arquivo de imagem", ".png", ),("Arquivo de imagem", ".jng"))) 
      print(self.digital) 
    

root = tk.Tk()
TelaCadastro(root)
root.mainloop()