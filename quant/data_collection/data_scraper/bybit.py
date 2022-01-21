from pybit import HTTP
from dateutil import parser


class Bybit:
    bybit_data = []
    @classmethod
    def get_bybit_data(cls):
        try:
            session = HTTP("https://api-testnet.bybit.com")
            data = session.public_trading_records(symbol="BTCUSD")
            result = data['result']
            exchange_bybit = []
            for res in result:
                timestamp = parser.parse(res['time'])
                adict = {"source": "bybit", "price": res["price"],
                         "taker_buy_volume": "", "taker_sell_volume": "", "timestamp": timestamp}
                if res['side'] == 'Sell':
                    adict["taker_sell_volume"] = res["qty"]
                else:
                    adict["taker_buy_volume"] = res["qty"]
                exchange_bybit.append(adict)
            cls.bybit_data = exchange_bybit
        except Exception as error:
            print(error)

