class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome}, Ano: {self.ano}, Likes:{self.likes}'



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome}, Ano: {self.ano}, Duração: {self.duracao}, Likes:{self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome}, Ano: {self.ano}, Temporadas: {self.temporadas} Likes:{self.likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome= nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

vingadores = Filme("vingadores - End Game", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
avatar = Filme('avatar', 2009, 181)
tbs = Serie('the boys', 2022, 4)

vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tbs.dar_likes()
tbs.dar_likes()
tbs.dar_likes()
tbs.dar_likes()
avatar.dar_likes()
avatar.dar_likes()
avatar.dar_likes()


filmes_e_series = [vingadores, avatar, atlanta, tbs]

for programa in filmes_e_series:
    print(programa)