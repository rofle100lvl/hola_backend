import sqlite3

from datetime import datetime


class DataBase:
    DATABASE = 'mydatabase.db'

    def __init__(self):
        conn = sqlite3.connect(self.DATABASE)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Kit(
                        id BIGINT NOT NULL PRIMARY KEY, 
                        name TEXT NOT NULL, 
                        count_of_numbers INTEGER NOT NULL
                        )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Question(
                                id BIGINT NOT NULL PRIMARY KEY,
                                name TEXT NOT NULL,
                                question TEXT NOT NULL
                                )""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS Relation(
                                id BIGINT NOT NULL PRIMARY KEY, 
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
        ans = cursor.fetchone()
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
