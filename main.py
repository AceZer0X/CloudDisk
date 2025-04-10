# app/main.py
from fastapi import FastAPI
from database import engine, Base
import files, folders, share, auth

# Инициализация базы данных
Base.metadata.create_all(bind=engine)

# Инициализация приложения FastAPI
app = FastAPI()

# Подключаем маршруты
app.include_router(files.router, prefix="/api", tags=["Files"])
app.include_router(folders.router, prefix="/api", tags=["Folders"])
app.include_router(share.router, prefix="/api", tags=["Share"])

# Убедимся, что сервер запустится на порту 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
