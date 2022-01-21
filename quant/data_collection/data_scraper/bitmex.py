from dateutil import parser
import requests


class Bitmex:
    bitmex_data = []
    @classmethod
    def get_bitmex_data(cls):
        try:
            result = requests.get("https://www.bitmex.com/api/v1/trade").json()
            exchange_bitmex = []
            for res in result:
                timestamp = parser.parse(res['timestamp'])
                adict = {"source": "bitmex", "price": res["price"],
                         "taker_buy_volume": "", "taker_sell_volume": "", "timestamp": timestamp}
                if res['side'] == 'Sell':
                    adict["taker_sell_volume"] = res["size"]
                else:
                    adict["taker_buy_volume"] = res["size"]
                exchange_bitmex.append(adict)
            cls.bitmex_data = exchange_bitmex
        except Exception as error:
            print(error)

