class classname():

    def __init__(self, nome, login, senha, digital, nivelAcesso):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.digital = digital
        self.nivelAcesso = nivelAcesso

    def getNome(self):
        return self.nome

    def getLogin(self):
        return self.login

    def getSenha(self):
        return self.senha

    def getDigital(self):
        return self.digital

    def getNivelAcesso(self):
        return self.nivelAcesso

    nome = property(fget=getNome)
    login = property(fget=getNome)
    senha = property(fget=getSenha)
    digital = property(fget=getDigital)
    nivelAcesso = property(fget=getNivelAcesso)
