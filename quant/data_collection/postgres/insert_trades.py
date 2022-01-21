import psycopg2
from config import config

from quant.data_collection.data_scraper import Bybit,Bitmex


def insert_trades(trades):
    """ insert multiple trades into the trades table  """
    sql = '''INSERT INTO trade(source, price, taker_buy_volume, taker_sell_volume, timestamp)
          VALUES( %(source)s, %(price)s, %(taker_buy_volume)s, %(taker_sell_volume)s, %(timestamp)s);'''
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,trades)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    data = []
    Bitmex.get_bitmex_data()
    bitmex_data = Bitmex.bitmex_data

    Bybit.get_bybit_data()
    bybit_data = Bybit.bybit_data

    data.extend(bitmex_data)
    data.extend(bybit_data)

    insert_trades(data)






