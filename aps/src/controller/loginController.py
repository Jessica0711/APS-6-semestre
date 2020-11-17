from src.controller import processarImagem
from src.dao import usuarioDao


def loginController(login, senha=None, img=None):
    dao = usuarioDao.UsuarioDAO()

    if senha is not None:
        return dao.findUserSenha(login, senha)

    if img is not None:
        r, c = processarImagem.processarImagem(img, 'login')
        return dao.findUserDigital(login, r[0], c[0])
