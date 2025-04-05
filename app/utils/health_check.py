from sqlalchemy import text
from app.db.session import engine

def check_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            return True
    except:
        return False