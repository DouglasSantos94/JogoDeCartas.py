from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    def valor_total_carta(self) -> int:
        valor_total = 0
        for valor_atributo in self.personagem.atributos.values():
            valor_total += valor_atributo
        return valor_total

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
