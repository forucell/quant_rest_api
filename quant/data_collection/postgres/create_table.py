import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    command = '''
            CREATE TABLE if not exists trade2 ( 
                trade_id SERIAL PRIMARY KEY,
                source TEXT,
                price FLOAT(5),
                taker_buy_volume TEXT, 
                taker_sell_volume TEXT, 
                timestamp TIMESTAMP WITH TIME ZONE,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            );
        '''
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()