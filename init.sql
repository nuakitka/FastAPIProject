-- Инициализация базы данных для проекта Fruit Management
-- Этот файл выполняется автоматически при первом запуске PostgreSQL контейнера

-- Создаем базу данных (если не существует)
-- CREATE DATABASE IF NOT EXISTS fruits;

-- Создаем пользователя (если не существует)
-- CREATE USER IF NOT EXISTS nuakitka WITH PASSWORD '1111';

-- Предоставляем права доступа
-- GRANT ALL PRIVILEGES ON DATABASE fruits TO nuakitka;

-- Создаем таблицу fruits (будет создана автоматически через SQLAlchemy)
-- CREATE TABLE IF NOT EXISTS fruits (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- Вставляем тестовые данные
-- INSERT INTO fruits (name) VALUES ('Apple'), ('Banana'), ('Orange');

-- Комментарий: Таблицы создаются автоматически через SQLAlchemy при запуске приложения
