from hardware.brewer import BrewerInterface


class BrewerFake(BrewerInterface):
    def __init__(self):
        self.__nb_appels_make_a_coffee = 0

    def make_a_coffee(self) -> bool:
        self.__nb_appels_make_a_coffee += 1
        return True

    def try_pull_water(self) -> bool:
        raise NotImplementedError()

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

