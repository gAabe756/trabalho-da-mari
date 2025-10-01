from model import StreamingModel, UsuarioModel

class StreamingController:
    def __init__(self):
        self.model = StreamingModel()
        self.usuario_model = UsuarioModel()

    def login(self, usuario, senha):
        return self.usuario_model.autenticar(usuario, senha)

    def adicionar_midia(self, titulo, genero, avaliacao, ano, idioma, temporada=0, episodio=0):
        self.model.adicionar_midia(titulo, genero, avaliacao, ano, idioma, temporada, episodio)

    def listar_disponiveis(self):
        return self.model.listar_disponiveis()

    def listar_destaque(self):
        return self.model.listar_destaque()

    def destacar_midia(self, indice):
        self.model.destacar_midia(indice)

    def remover_midia(self, indice):
        self.model.remover_midia(indice)

    def remover_destaque(self, indice):
        self.model.remover_destaque(indice)
