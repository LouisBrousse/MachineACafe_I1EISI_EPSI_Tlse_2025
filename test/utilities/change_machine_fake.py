from hardware.changemachine import ChangeMachineInterface
from hardware.coincode import CoinCode


class ChangeMachineFake(ChangeMachineInterface):
    def __init__(self):
        self.__flush_done = False
    
    def register_money_inserted_callback(self, callback: CoinCode = None) -> None:
        raise NotImplementedError()

    def flush_stored_money(self) -> None:
        self.__flush_done = True

    def collect_stored_money(self) -> None:
        raise NotImplementedError()

    def drop_cashback(self, coin_code: CoinCode) -> bool:
        raise NotImplementedError()

    def total_argent_encaissé_en_centimes(self) -> int:
        return 50

