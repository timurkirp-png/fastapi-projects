from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import get_setting

setting = get_setting()

if not setting.DATABASE_URL:
    raise ValueError("DATABASE_URL не найден. Проверь файл .env в корне проекта.")

engine = create_engine(setting.DATABASE_URL)

Session_local = sessionmaker(bind=engine)

def get_db():
    # ФУНКЦИЯ ДЛЯ ИНЬЕКЦИИ СЕССИИ БД
    db = Session_local()
    try:
        yield db
    finally:
        db.close()
