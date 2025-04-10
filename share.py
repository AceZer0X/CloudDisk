# app/share.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Share, File
import uuid

router = APIRouter()

# Создание ссылки для шаринга файла
@router.post("/share/{file_id}", response_model=Share)
async def share_file(file_id: int, db: Session = Depends(SessionLocal)):
    db_file = db.query(File).filter(File.id == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")

    share_link = str(uuid.uuid4())  # Генерация уникальной ссылки
    db_share = Share(file_id=file_id, link=share_link)
    db.add(db_share)
    db.commit()
    db.refresh(db_share)
    return db_share
