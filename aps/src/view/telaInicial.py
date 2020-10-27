import tkinter as tk


class TelaInicial:

    def __init__(self, master=None):
        self.widget1 = tk.Frame(master)
        self.widget1.pack()
        self.msg = tk.Label(self.widget1, text="Login de Usuário")
        self.msg["font"] = ("Verdana", "18", "italic", "bold")
        self.msg.pack()
        self.cadastrar = tk.Button(self.widget1)
        self.cadastrar["text"] = "Cadastrar novo usuário"
        self.cadastrar["width"] = 20
        self.cadastrar["font"] = ("Calibri", "10")
        self.cadastrar.pack()
        self.sair = tk.Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()


root = tk.Tk()
TelaInicial(root)
root.mainloop()
