# Простой Makefile для запуска проекта

.PHONY: help build up down logs clean test

# Показать помощь
help:
	@echo "Доступные команды:"
	@echo "  make build     - Собрать все Docker образы"
	@echo "  make up        - Запустить все сервисы"
	@echo "  make down      - Остановить все сервисы"
	@echo "  make logs      - Показать логи всех сервисов"
	@echo "  make clean     - Очистить все контейнеры и образы"
	@echo "  make test      - Протестировать API"

# Собрать образы
build:
	@echo "Собираем Docker образы..."
	docker-compose build

# Запустить все сервисы
up:
	@echo "Запускаем все сервисы..."
	docker-compose up -d

# Остановить все сервисы
down:
	@echo "Останавливаем все сервисы..."
	docker-compose down

# Показать логи
logs:
	@echo "Показываем логи..."
	docker-compose logs -f

# Очистить все
clean:
	@echo "Очищаем контейнеры и образы..."
	docker-compose down -v
	docker system prune -f

# Тестировать API
test:
	@echo "Тестируем API..."
	@echo "GET /fruits:"
	curl -s http://localhost:8000/fruits || echo "API не отвечает"
	@echo ""
	@echo "POST /fruits:"
	curl -s -X POST http://localhost:8000/fruits -H "Content-Type: application/json" -d '{"name":"Apple"}' || echo "API не отвечает"