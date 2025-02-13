from hardware.brewer import BrewerInterface


class BrewerFake(BrewerInterface):
    def __init__(self):
        self.__nb_appels_make_a_coffee = 0
        self.__presence_d_eau = True
        self.__defaillance = False

    def make_a_coffee(self) -> bool:
        if self.__defaillance:
            return False
        else:
            self.__nb_appels_make_a_coffee += 1
            return True

    def try_pull_water(self) -> bool:
        return self.__presence_d_eau

    def pour_milk(self) -> bool:
        raise NotImplementedError()

    def pour_water(self) -> bool:
        raise NotImplementedError()

    def pour_sugar(self) -> bool:
        raise NotImplementedError()

    def pour_chocolate(self) -> bool:
        raise NotImplementedError()

    def nb_appels_make_a_coffee(self) -> int:
        return self.__nb_appels_make_a_coffee

    def simuler_absence_d_eau(self) -> bool :
        self.__presence_d_eau = False

    def simuler_defaillance(self) -> bool:
        self.__defaillance = True

    