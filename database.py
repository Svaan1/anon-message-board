from sqlalchemy import create_engine, text
import os 

class Database:
    def __init__(self):
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.connection = self.engine.connect()
        self.start_table()
    
    def start_table(self):
        statement =  text("CREATE TABLE IF NOT EXISTS messages (id SERIAL, body varchar(100))")
        self.connection.execute(statement)
        self.connection.commit()

    def insert(self, body):
        statement = text("INSERT INTO messages (body) VALUES (:body)").bindparams(body=body)
        self.connection.execute(statement)
        self.connection.commit()
    
    def get(self):
        statement = text("SELECT * FROM messages ORDER BY id DESC LIMIT 5")
        result = self.connection.execute(statement)
        result = [post[1] for post in result.fetchall()]
        return result