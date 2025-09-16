# Fruit Management App

Простое приложение для управления фруктами с FastAPI backend и React frontend.

## Структура проекта

- `backend/` - FastAPI приложение с PostgreSQL базой данных
- `frontend/` - React приложение с Vite

## Настройка базы данных PostgreSQL

1. **Установите PostgreSQL** (если еще не установлен):
```bash
# macOS (с Homebrew)
brew install postgresql
brew services start postgresql

# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib
```

2. **Создайте базу данных**:
```bash
# Войдите в PostgreSQL
psql -U postgres

# Создайте базу данных
CREATE DATABASE fruits_db;

# Создайте пользователя (опционально)
CREATE USER fruits_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE fruits_db TO fruits_user;

# Выйдите
\q
```

3. **Настройте переменные окружения**:
```bash
# Установите переменную окружения
export DATABASE_URL="postgresql://postgres:your_password@localhost:5432/fruits_db"

# Или создайте файл .env в папке backend с содержимым:
# DATABASE_URL=postgresql://postgres:your_password@localhost:5432/fruits_db
```

## Запуск проекта

### 🐳 Docker (рекомендуется)

**Быстрый запуск:**
```bash
# Собрать и запустить все сервисы
make build && make up

# Или использовать docker-compose напрямую
docker-compose up --build
```

**Режим разработки:**
```bash
# Запуск с hot reload
make dev

# Или
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

**Полезные команды:**
```bash
make help     # Показать все доступные команды
make logs     # Показать логи всех сервисов
make restart  # Перезапустить сервисы
make down     # Остановить все сервисы
make clean    # Очистить все контейнеры и образы
```

**Доступ к приложению:**
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- PostgreSQL: localhost:5432


**Backend:**
```bash
cd backend
pip install -r requirements.txt
cp env_template.txt .env
# Отредактируйте .env файл
python main.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `GET /fruits` - Получить список всех фруктов
- `POST /fruits` - Добавить новый фрукт
- `DELETE /fruits` - Удалить фрукт

## Функциональность

- Просмотр списка фруктов
- Добавление новых фруктов
- Удаление существующих фруктов
- Данные сохраняются в postgres базе данных
