import sqlite3

class DBConnection:
    def __init__(self, db_name="two_factor_auth.db"):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    otp TEXT
                  );'''
        self.conn.execute(query)
        self.conn.commit()

    def get_connection(self):
        if not self.conn:
            self.connect()
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
