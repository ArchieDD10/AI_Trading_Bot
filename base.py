from abc import ABC, abstractmethod


class BrokerBase(ABC):
    @abstractmethod
    def place_order(
        self,
        direction: str,
        entry_price: float,
        stop_loss: float,
        take_profit: float,
        timestamp
    ):
        pass

    @abstractmethod
    def close_position(self, exit_price: float, timestamp):
        pass

    @abstractmethod
    def get_open_position(self):
        pass