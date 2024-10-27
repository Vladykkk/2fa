from dal.db_connection import DBConnection

class UserRepository:
    def __init__(self):
        self.db = DBConnection()

    def find_user(self, username):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()

    def update_otp(self, username, otp):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET otp=? WHERE username=?", (otp, username))
        conn.commit()

    def add_user(self, username, password):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
