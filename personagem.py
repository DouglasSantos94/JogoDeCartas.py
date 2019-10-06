from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    #Construtor fornecido, nao deve ser alterado
    def __init__(self, energia: int, habilidade: int,
                 velocidade: int, resistencia: int, tipo: Tipo):
        self.__atributos = {'energia': energia,
                            'habilidade': habilidade,
                            'velocidade': velocidade,
                            'resistencia': resistencia}
        self.__tipo = tipo

    @property
    def tipo(self) -> Tipo:
        return self.__tipo

    @property
    def energia(self) -> int:
        return self.__atributos['energia']

    @property
    def habilidade(self) -> int:
        return self.__atributos['habilidade']

    @property
    def velocidade(self) -> int:
        return self.__atributos['velocidade']

    @property
    def resistencia(self) -> int:
        return self.__atributos['resistencia']

    @property
    def atributos(self):
        return self.__atributos
