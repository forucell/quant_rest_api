from clean_architecture.domain import (
    ValidRequestObject,
    UseCase,
    ResponseSuccess,
)
from quant.entity import TradeEntity, ListEntity


class ListTradeRequestObject(ValidRequestObject):
    def __init__(self, filters):
        self.filters = filters

    @classmethod
    def from_dict(cls, filters):
        return ListTradeRequestObject(filters)


class ListTrade(UseCase):
    def __init__(self, trade_repo):
        self.trade_repo = trade_repo

    def convert_to_entity(self, trades):
        trades["items"] = [
            TradeEntity.from_dict(
                {
                    "trade_id": trade.trade_id,
                    "source": trade.source,
                    "price": trade.price,
                    "taker_buy_volume": trade.taker_buy_volume,
                    "taker_sell_volume": trade.taker_sell_volume,
                    "timestamp": trade.timestamp,
                    "created_at": trade.created_at

                }
            )
            for trade in trades["items"]
        ]
        return ListEntity.from_dict(trades)

    def process_request(self, request_object):
        trades = self.trade_repo.list(**request_object.filters)
        trades = self.convert_to_entity(trades)
        return ResponseSuccess(200, trades)
