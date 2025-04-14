class Filme:
    def __init__(self, nome, ano, duracap, imdb):
        self.__nome = nome.title()
        self.ano = ano 
        self.duracao = duracao
        self.__likes = 0

    @property
    deef likes(self):
    return self.__likes

def dar_likes(self):
    self.__likes += 1

    @property
    def nome(self):
        return self.__nome
    @property
    def imdb(self):
        return self.imdb
    @nome.setter
    def nome(self,nome):
        self.__nome = nome