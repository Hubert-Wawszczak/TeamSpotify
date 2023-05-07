import mysql.connector

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(

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

    def get_room_by_id(self, room_id):
        query = "SELECT * FROM Room WHERE id = %s"
        values = (room_id,)
        self.cursor.execute(query, values)
        room = self.cursor.fetchone()
        return room

    def get_room_by_name(self, room_name):
        query = "SELECT * FROM Room WHERE nazwa = %s"
        values = (room_name,)
        self.cursor.execute(query, values)
        room = self.cursor.fetchone()
        return room

    def create_room(self, room):
        query = "INSERT INTO Room (nazwa, haslo) VALUES (%s, %s)"
        values = (room.nazwa, room.haslo)
        self.cursor.execute(query, values)
        room_id = self.cursor.lastrowid
        self.db.commit()
        return room_id

    def update_room(self, room_id, room):
        query = "UPDATE Room SET nazwa = %s, haslo = %s WHERE id = %s"
        values = (room.nazwa, room.haslo, room_id)
        self.cursor.execute(query, values)
        self.db.commit()

    def delete_room(self, room_id):
        query = "DELETE FROM Room WHERE id = %s"
        values = (room_id,)
        self.cursor.execute(query, values)
        self.db.commit()

    def get_room_by_id(self, room_id):
        query = "SELECT * FROM Room WHERE id = %s"
        values = (room_id,)
        self.cursor.execute(query, values)
        room = self.cursor.fetchone()
        return room

    def get_room_by_name(self, room_name):
        query = "SELECT * FROM Room WHERE nazwa = %s"
        values = (room_name,)
        self.cursor.execute(query, values)
        room = self.cursor.fetchone()
        return room

    def create_room(self, room):
        query = "INSERT INTO Room (nazwa, haslo) VALUES (%s, %s)"
        values = (room.nazwa, room.haslo)
        self.cursor.execute(query, values)
        room_id = self.cursor.lastrowid
        self.db.commit()
        return room_id

    def update_room(self, room_id, room):
        query = "UPDATE Room SET nazwa = %s, haslo = %s WHERE id = %s"
        values = (room.nazwa, room.haslo, room_id)
        self.cursor.execute(query, values)
        self.db.commit()

    def delete_room(self, room_id):
        query = "DELETE FROM Room WHERE id = %s"
        values = (room_id,)
        self.cursor.execute(query, values)
        self.db.commit()