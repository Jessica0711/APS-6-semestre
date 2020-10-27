from src.corn import connectionFactory as connectionFac


class UsuarioDAO():

    def __init__(self):
        self.conexao = connectionFac.ConnectionFactory().getConnection()
        self.connection = self.conexao.cursor()

    def create(self, usuario):
        self.connection.execute("""
        INSERT INTO usuarios (nome, login, senha, digital) VALUES (?,?,?,?)
        """, (usuario.getNome(), usuario.getLogin(), usuario.getSenha(),
              usuario.getDigital()))
        self.conexao.commit()

    def read(self):
        self.connection.execute('SELECT * FROM usuarios')
        return self.connection.fetchall()

    def update(self, login, senha):
        self.connection.execute("""
        UPDATE usuarios SET login = ?, senha = ?
        """, login, senha)
        self.conexao.commit()

    def delete(self, id):
        self.connection.execute('DELETE FROM usuarios WHERE id = ?', id)

    def findUser(self, login, digital):
        self.connection.execute("""
        SELECT FROM usuarios WHERE login = ? AND digital = ?
        """, login, digital)
        return self.connection.fetchall()
