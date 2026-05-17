# 1. Базовый образ
FROM python:3.12-slim

# 2. Рабочая папка внутри контейнера
WORKDIR /app

# 3. Копируем файлы проекта
COPY main.py .
COPY requirements.txt .

# 4. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# 5. Открываем порт
EXPOSE 8000

# 6. Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]