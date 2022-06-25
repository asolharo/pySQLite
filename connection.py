import sqlite3

database = "database.db"


class DB:
    def execute_query(self, query, params=()):
        with sqlite3.connect(database) as conn:
            self.cursor = conn.cursor()
            result = self.cursor.execute(query, params)

            conn.commit()
            return result
