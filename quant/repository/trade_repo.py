from .trade_abc_repo import TradeAbcRepository
from quant.models import Trade

class TradeRepository(TradeAbcRepository):
    def list(self, source,limit,_from):
        if source != "all_exchange":
            trades = Trade.query.filter(Trade.source == source).filter(Trade.timestamp >= _from).limit(limit).all()
        else:
            trades = Trade.query.filter(Trade.timestamp >= _from).limit(limit).all()
        return {
            "items": trades
        }
