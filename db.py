import sqlite3

from datetime import datetime


class DataBase:
    DATABASE = 'mydatabase.db'

    def __init__(self):
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Kit(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                        name TEXT NOT NULL
                        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Question(
                                id INTEGER NOT NULL PRIMARY KEY,
                                question TEXT NOT NULL
                                )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Relation(
                                id INTEGER NOT NULL PRIMARY KEY, 
                                kit_id BIGINT NOT NULL,
                                question_id BIGINT NOT NULL 
                                )""")

    def get_questions_by_kit(self, kit):
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute(f"""select * from Question where
                            Question.id in (
                            select Relation.question_id from Relation where Relation.kit_id = {kit}
)""")
        conn.commit()
        ans = cursor.fetchall()
        cursor.close()
        conn.close()
        return ans

    def get_kits(self):
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Kit")
        conn.commit()
        ans = cursor.fetchall()
        cursor.close()
        conn.close()
        return ans

    def clear_tables(self):
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Kit")
        cursor.execute(f"DELETE FROM Question")
        conn.commit()
        cursor.close()
        conn.close()

    def add_kit(self, kit):
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO Kit (name) values ('{kit}')")
        conn.commit()
        cursor.close()
        conn.close()

    def add_question(self, question):
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO Question (question) values ('{question}')")
        conn.commit()
        cursor.close()
        conn.close()

    def add_relation(self, kit, question):
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id from Kit where name = '{kit}'")
        conn.commit()
        kit_id = cursor.fetchone()[0]
        cursor.execute(f"SELECT id from Question where question = '{question}'")
        conn.commit()
        question_id = cursor.fetchone()[0]
        cursor.execute(f"INSERT INTO Relation (kit_id, question_id) values ({kit_id}, {question_id})")
        conn.commit()
        cursor.close()
        conn.close()
