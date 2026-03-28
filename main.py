from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.utils import days_until_new_year

app = FastAPI(
    title="New Year Counter API",
    description="API для подсчета дней до Нового года",
    version="1.0.0"
)

@app.get("/info")
async def get_info():
    """
    Возвращает количество дней до наступления Нового года.
    
    Returns:
        JSON: Объект с полем days_before_new_year
    """
    days = days_until_new_year()
    return JSONResponse(
        content={"days_before_new_year": days},
        status_code=200
    )

@app.get("/health")
async def health_check():
    """
    Эндпоинт для проверки работоспособности сервиса.
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4200)