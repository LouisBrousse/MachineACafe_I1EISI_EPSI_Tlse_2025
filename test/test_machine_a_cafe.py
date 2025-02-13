import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


import unittest

from src.machine_a_cafe import MachineACafe
from src.piece import Piece
from test.utilities.brewer_fake import BrewerFake


class TestMachineACafe(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine à café
        brewer = BrewerFake()
        machine_a_cafe = MachineACafe(brewer)
        # QUAND on insère 50cts
        machine_a_cafe.inserer(Piece.CinquanteCentimes, brewer)
        # ALORS un café est servi
        self.assertEqual(1, brewer.nb_appels_make_a_coffee())

    def test_cas_absence_argent(self):
        # ETANT DONNE une machine à café
        brewer = BrewerFake()
        MachineACafe(brewer)
        # ALORS aucun café n'est servi
        self.assertEqual(0, brewer.nb_appels_make_a_coffee())

    def test_cas_absence_eau(self):
        #ETANT DONNE une machine à café n'ayant plus d'eau
        brewer = BrewerFake()
        brewer.simuler_absence_d_eau()
        machine_a_cafe = MachineACafe(brewer)
        #QUAND on insère 50cts
        machine_a_cafe.inserer(Piece.CinquanteCentimes, brewer)
        #ALORS la somme est restituée
        # self.assertEqual(True, change.flush_done())
        #(ET aucun café n'est servi)
        self.assertEqual(0, brewer.nb_appels_make_a_coffee())

    def test_cas_absence_cafe(self):
        # ETANT DONNE une machine à café n'ayant pas de café
        brewer = BrewerFake()
        brewer.simuler_defaillance()
        machine_a_cafe = MachineACafe(brewer)
        # QUAND on insère 50cts
        machine_a_cafe.inserer(Piece.CinquanteCentimes, brewer)
        # (ALORS le café n'est pas servi)
        self.assertEqual(0, brewer.nb_appels_make_a_coffee())
        # ET la machine rend l'argent
    
if __name__ == '__main__':
    unittest.main()
