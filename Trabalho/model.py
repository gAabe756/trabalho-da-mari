class Midia:
    def __init__(self, titulo, genero, avaliacao, ano, idioma, temporada=0, episodio=0):
        self.titulo = titulo
        self.genero = genero
        self.avaliacao = avaliacao
        self.ano = ano
        self.idioma = idioma
        self.temporada = temporada
        self.episodio = episodio

    def descricao(self):
        if self.genero == "Filme":
            return f"🎬 {self.titulo} | Nota: {self.avaliacao} | Ano: {self.ano} | Idioma: {self.idioma}"
        else:
            return f"📺 {self.titulo} | Nota: {self.avaliacao} | Ano: {self.ano} | Idioma: {self.idioma} | Temp: {self.temporada} | Ep: {self.episodio}"

class Filme(Midia):
    def __init__(self, titulo, avaliacao, ano, idioma):
        super().__init__(titulo, "Filme", avaliacao, ano, idioma)

class Serie(Midia):
    def __init__(self, titulo, avaliacao, ano, idioma, temporada, episodio):
        super().__init__(titulo, "Série", avaliacao, ano, idioma, temporada, episodio)

class Anime(Midia):
    def __init__(self, titulo, avaliacao, ano, idioma, temporada, episodio):
        super().__init__(titulo, "Anime", avaliacao, ano, idioma, temporada, episodio)

class StreamingModel:
    def __init__(self):
        self.midia_disponiveis = []
        self.midia_destaque = []

    def adicionar_midia(self, titulo, genero, avaliacao, ano, idioma, temporada=0, episodio=0):
        if genero == "Filme":
            nova = Filme(titulo, avaliacao, ano, idioma)
        elif genero == "Série":
            nova = Serie(titulo, avaliacao, ano, idioma, temporada, episodio)
        elif genero == "Anime":
            nova = Anime(titulo, avaliacao, ano, idioma, temporada, episodio)
        else:
            raise ValueError("Gênero inválido")
        self.midia_disponiveis.append(nova)

    def listar_disponiveis(self):
        return self.midia_disponiveis

    def listar_destaque(self):
        return self.midia_destaque

    def remover_midia(self, indice):
        if 0 <= indice < len(self.midia_disponiveis):
            self.midia_disponiveis.pop(indice)

    def destacar_midia(self, indice):
        if 0 <= indice < len(self.midia_disponiveis):
            midia = self.midia_disponiveis.pop(indice)
            self.midia_destaque.append(midia)

    def remover_destaque(self, indice):
        if 0 <= indice < len(self.midia_destaque):
            midia = self.midia_destaque.pop(indice)
            self.midia_disponiveis.append(midia)

class UsuarioModel:
    def __init__(self):
        self.usuario = "hiro"
        self.senha = "vendetta"

    def autenticar(self, usuario, senha):
        return usuario == self.usuario and senha == self.senha
