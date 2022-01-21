import abc


class TradeAbcRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def list(self, filters):
        pass
