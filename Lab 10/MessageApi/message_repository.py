import os
import sqlite3
from contextlib import closing
from typing import Optional

class MessageRepository:
    def __init__(self):
        self.db_path = os.getenv('DB_PATH', 'messages.db')

        with closing(sqlite3.connect(self.db_path)) as connection:
            connection.execute('''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY,
                    message TEXT NOT NULL
                )
            ''')
            connection.commit()

        
    def save_message(self, message) -> int:
        with closing(sqlite3.connect(self.db_path)) as connection:
            cursor = connection.execute(
                'INSERT INTO messages (message) VALUES (?)',
                (message,)
            )
    
            connection.commit()
            return cursor.lastrowid

    def get_message(self, id: int) -> Optional[str]:
        with closing(sqlite3.connect(self.db_path)) as connection:
            cursor = connection.execute(
                'SELECT message FROM messages WHERE id = ?',
                (id,)
            )

            result = cursor.fetchone()

            if result is None:
                return None

            return result[0]