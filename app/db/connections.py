import psycopg2
import os


class Connection:
    def __init__(self):
        self.host=os.getenv("DB_HOST","localhost")
        self.port=os.getenv("DB_PORT", "5432")
        self.user=os.getenv("DB_USER", "user")
        self.password=os.getenv("DB_PASSWORD", "postgress")
        self.dbname=os.getenv("DB_NAME", "mood_music") 
    
    def get_conn(self):
        conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            dbname=self.dbname,
        )
        return conn