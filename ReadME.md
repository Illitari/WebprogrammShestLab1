# New Year Counter API

Простое REST API на FastAPI, которое возвращает количество дней до наступления Нового года.

## 🚀 Возможности

- Эндпоинт `/info` - возвращает JSON с количеством дней до Нового года
- Эндпоинт `/health` - проверка работоспособности сервиса
- Контейнеризация с помощью Docker
- Автоматическая документация API (Swagger UI и ReDoc)
- Тестирование с использованием pytest

## 📋 Требования

- Python 3.11+
- Docker (опционально)
- Docker Compose (опционально)

## 🛠️ Локальный запуск

### Установка зависимостей

```bash
pip install -r requirements.txt


## Curl запрос в powerhell

Invoke-RestMethod -Uri http://localhost:4200/info