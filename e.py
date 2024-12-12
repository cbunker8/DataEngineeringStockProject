import yfinance as yf
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os
import numpy as np
from psycopg2.extras import RealDictCursor
import time

####################################################

load_dotenv()


db_config = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


def connect_to_db():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def create_tables():
    try:
        conn = connect_to_db()
        if not conn:
            return

        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS stock (
                ticker TEXT,
                date TIMESTAMP,
                open FLOAT,
                high FLOAT,
                low FLOAT,
                close FLOAT,
                volume BIGINT,
                PRIMARY KEY (ticker, date)  -- Composite primary key
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("Tables created successfully.")
    except Exception as e:
        print(f"Error creating tables: {e}")

def fetch_stock(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="5d", interval="1d")  
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None


def insert_stock(ticker, data):
    try:
        conn = connect_to_db()
        if not conn:
            return

        cur = conn.cursor()
        query = """
            INSERT INTO stock (ticker, date, open, high, low, close, volume) 
            VALUES %s
            ON CONFLICT (ticker, date) DO UPDATE SET
                open = EXCLUDED.open,
                high = EXCLUDED.high,
                low = EXCLUDED.low,
                close = EXCLUDED.close,
                volume = EXCLUDED.volume;
        """

    

        values = [
            (ticker, row["Date"], row["Open"], row["High"], row["Low"], row["Close"], row["Volume"])
            for _, row in data.iterrows()
        ]
        execute_values(cur, query, values)
        conn.commit()
        cur.close()
        conn.close()
        print(f"Data for {ticker} inserted successfully.")
    except Exception as e:
        print(f"Error inserting data for {ticker}: {e}")


def main():
    create_tables()

    tickers = ["RIVN","TSLA","LCID","F","STLA","GM"]  
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = fetch_stock(ticker)
        if data is not None and not data.empty:
            insert_stock(ticker, data)
        else:
            print(f"No data found for {ticker}.")

if __name__ == "__main__":
    main()
