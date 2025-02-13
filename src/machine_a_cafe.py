from hardware.brewer import BrewerInterface
from piece import Piece


class MachineACafe:
    def __init__(self, brewer: BrewerInterface):
        self.__brewer = brewer

    def inserer(self, pièce: Piece, brewer: BrewerInterface):
        if self.verifierSiPresenceEau(brewer):
            self.__brewer.make_a_coffee()

    def verifierSiPresenceEau(self, brewer: BrewerInterface)-> bool: 
        return self.__brewer.try_pull_water()

