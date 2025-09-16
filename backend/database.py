import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

# Получаем URL базы данных из переменных окружения
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://nuakitka:1111@localhost:5432/fruits")

# Создаем движок с настройками для PostgreSQL
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Проверяем соединение перед использованием
    echo=False  # Установите True для отладки SQL запросов
)

# Создаем фабрику сессий
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Создаем scoped session для использования в приложении
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Базовый класс для моделей
Base = declarative_base()


