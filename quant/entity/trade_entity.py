from clean_architecture.entity import Entity


class TradeEntity(Entity):
    def __init__(
        self,
        trade_id,
        source,
        price,
        taker_buy_volume,
        taker_sell_volume,
        timestamp,
        created_at,
    ):
        self.trade_id = trade_id
        self.source = source
        self.price = price
        self.taker_buy_volume = taker_buy_volume
        self.taker_sell_volume = taker_sell_volume
        self.timestamp = timestamp
        self.created_at = created_at

    @classmethod
    def from_dict(cls, adict):
        trade = TradeEntity(
            trade_id=adict.get("trade_id"),
            source=adict.get("source"),
            price=adict.get("price"),
            taker_buy_volume=adict.get("taker_buy_volume"),
            taker_sell_volume=adict.get("taker_sell_volume"),
            timestamp=adict.get("timestamp"),
            created_at=adict.get("created_at")
        )
        return trade
