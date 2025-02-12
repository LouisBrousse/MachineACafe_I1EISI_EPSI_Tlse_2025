from hardware.brewer import BrewerInterface
from piece import Piece


class MachineACafe:
    def __init__(self, brewer: BrewerInterface):
        self.__brewer = brewer

    def inserer(self, pièce: Piece):
        self.__brewer.make_a_coffee()