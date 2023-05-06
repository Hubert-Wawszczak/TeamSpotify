import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="mysql58.mydevil.net",
            user="m1065_admin",
            password="PeBv3rYg7iYP3zQEQD34",
            database="m1065_spotifyroom"
        )
        self.cursor = self.db.cursor()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.db.commit()
        return self.cursor

    def get_user_by_id(self, user_id):
        query = "SELECT * FROM użytkownik WHERE id = %s"
        values = (user_id,)
        self.cursor.execute(query, values)
        user = self.cursor.fetchone()
        return user

    def create_user(self, user):
        query = "INSERT INTO użytkownik (nick) VALUES (%s)"
        values = (user.nick,)
        self.cursor.execute(query, values)
        user_id = self.cursor.lastrowid
        self.db.commit()
        return user_id
