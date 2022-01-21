from quant.extensions import db
from datetime import datetime

datetime.utcnow()


class Trade(db.Model):
    trade_id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String)
    price = db.Column(db.Float)
    taker_buy_volume = db.Column(db.String)
    taker_sell_volume = db.Column(db.String)
    timestamp = db.Column(db.DateTime(timezone=True))
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now())