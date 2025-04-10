# app/files.py
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from database import SessionLocal
from models import File, User
from schemas import FileCreate, FileOut
import os
import shutil

router = APIRouter()

# Загрузка файла
@router.post("/files/", response_model=FileOut)
async def upload_file(file: UploadFile = File(...), db: Session = Depends(SessionLocal)):
    # Сохранение файла на сервере
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    db_file = File(filename=file.filename, content_type=file.content_type, path=file_path, owner_id=1)  # hardcoded user_id
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

# Скачивание файла
@router.get("/files/{file_id}", response_model=FileOut)
async def get_file(file_id: int, db: Session = Depends(SessionLocal)):
    db_file = db.query(File).filter(File.id == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return db_file

# Удаление файла
@router.delete("/files/{file_id}")
async def delete_file(file_id: int, db: Session = Depends(SessionLocal)):
    db_file = db.query(File).filter(File.id == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    os.remove(db_file.path)
    db.delete(db_file)
    db.commit()
    return {"message": "File deleted successfully"}
