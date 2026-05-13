import psycopg2
import os

class Connection:
    """класс для подключения к базе данных берет данные из .env файла"""
    def __init__(self):
        self.host=os.getenv("DB_HOST","localhost")
        self.port=os.getenv("DB_PORT", "5432")
        self.user=os.getenv("DB_USER", "user")
        self.password=os.getenv("DB_PASSWORD", "postgress")
        self.dbname=os.getenv("DB_NAME", "class_register") 
    
    def get_conn(self) -> psycopg2.connect:
        """функция которая возвращает подключение"""
        conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.dbname,
        )
        return conn