from schema import Schema, And, Optional, Or
from clean_architecture.serializer import Serializer


class ListTradeEncoder(Serializer):
    schema = Schema(
        {
            "items": [
                {
                    "trade_id": int,
                    "source": str,
                    "price": float,
                    "taker_buy_volume": str,
                    "taker_sell_volume": str,
                    "timestamp":str,
                    "created_at": str,
                }
            ],
        },
        ignore_extra_keys=True,
    )