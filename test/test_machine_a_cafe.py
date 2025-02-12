import unittest

from machine_a_cafe import MachineACafe
from piece import Piece
from utilities.brewer_fake import BrewerFake


class TestMachineACafe(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine à café
        brewer = BrewerFake()
        machine_a_cafe = MachineACafe(brewer)

        # QUAND on insère 50cts
        machine_a_cafe.inserer(Piece.CinquanteCentimes)

        # ALORS un café est servi
        self.assertEqual(1, brewer.nb_appels_make_a_coffee())

    def test_cas_absence_argent(self):
        # ETANT DONNE une machine à café
        brewer = BrewerFake()
        MachineACafe(brewer)

        # ALORS aucun café n'est servi
        self.assertEqual(0, brewer.nb_appels_make_a_coffee())


if __name__ == '__main__':
    unittest.main()
