import sqlite3
import csv
from datetime import datetime

def initialize_db(db_path="modifiers.sqlite"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # create table
    cursor.execute("DROP TABLE IF EXISTS INSTRUMENT_PRICE_MODIFIER")
    cursor.execute("""
        CREATE TABLE INSTRUMENT_PRICE_MODIFIER (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            MULTIPLIER REAL NOT NULL
        )
    """)
    cursor.executemany("""
        INSERT INTO INSTRUMENT_PRICE_MODIFIER (NAME, MULTIPLIER)
        VALUES (?, ?)
    """, [
        ("INSTRUMENT1", 1.1),
        ("INSTRUMENT2", 0.9),
        ("INSTRUMENT3", 1.05)
    ])

    # Prices
    cursor.execute("DROP TABLE IF EXISTS RAW_PRICES")
    cursor.execute("""
        CREATE TABLE RAW_PRICES (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            DATE TEXT,
            VALUE REAL
        )
    """)

    # Loading data from csv
    try:
        with open("data/example_input.csv", newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) != 3:
                    continue
                name, date_str, value_str = row
                try:
                    date_obj = datetime.strptime(date_str.strip(), "%d-%b-%Y")
                    iso_date = date_obj.strftime("%Y-%m-%d")
                    value = float(value_str)
                    cursor.execute(
                        "INSERT INTO RAW_PRICES (NAME, DATE, VALUE) VALUES (?, ?, ?)",
                        (name.strip(), iso_date, value)
                    )
                except Exception as e:
                    print("Error:", row, e)
    except FileNotFoundError:
        print("File not found")

    conn.commit()
    conn.close()
    print("Database initialized and data loaded.")

if __name__ == "__main__":
    initialize_db()
