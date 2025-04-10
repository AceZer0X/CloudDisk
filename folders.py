# app/folders.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Folder
from schemas import FolderCreate, FolderOut

router = APIRouter()

# Создание папки
@router.post("/folders/", response_model=FolderOut)
async def create_folder(folder: FolderCreate, db: Session = Depends(SessionLocal)):
    db_folder = Folder(name=folder.name, owner_id=1)  # hardcoded user_id
    db.add(db_folder)
    db.commit()
    db.refresh(db_folder)
    return db_folder

# Навигация по папкам
@router.get("/folders/{folder_id}", response_model=FolderOut)
async def get_folder(folder_id: int, db: Session = Depends(SessionLocal)):
    db_folder = db.query(Folder).filter(Folder.id == folder_id).first()
    if db_folder is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    return db_folder
