# Простой рабочий Dockerfile для frontend
FROM node:18

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код
COPY . .

# Собираем приложение
RUN npm run build

# Устанавливаем serve для запуска статических файлов
RUN npm install -g serve

# Открываем порт
EXPOSE 3000

# Запускаем приложение
CMD ["serve", "-s", "dist", "-l", "3000"]