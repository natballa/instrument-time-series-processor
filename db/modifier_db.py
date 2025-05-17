import sqlite3

class ModifierDB:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def get_multiplier(self, instrument_name: str) -> float:
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT MULTIPLIER FROM INSTRUMENT_PRICE_MODIFIER WHERE NAME = ?",
            (instrument_name,)
        )
        row = cursor.fetchone()
        return row[0] if row else 1.0
