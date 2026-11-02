import os
import psycopg2
from typing import Optional




class MessageRepository:
    def __init__(self):
        self.create_table()

        
    def save_message(self, message) -> int:
        

    def get_message(self, id: int) -> str:
        # TODO: return message with id from storage
        pass
