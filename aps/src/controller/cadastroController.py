from src.controller import processarImagem
from src.model import usuario
from src.dao import usuarioDao


def cadastroController(img, nome, login, senha, nivelAcesso):
    r, c = processarImagem.processarImagem(img, 'cadastro')
    user = usuario.Usuario(nome, login, senha, nivelAcesso, r[0], c[0])
    dao = usuarioDao.UsuarioDAO()
    user = dao.create(user)
