# app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

# Схема для пользователя
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True

# Схема для файлов
class FileBase(BaseModel):
    filename: str
    content_type: str

class FileCreate(FileBase):
    pass

class FileOut(FileBase):
    id: int
    owner_id: int
    path: str
    class Config:
        orm_mode = True

# Схема для папок
class FolderBase(BaseModel):
    name: str

class FolderCreate(FolderBase):
    pass

class FolderOut(FolderBase):
    id: int
    owner_id: int
    parent_id: Optional[int] = None
    class Config:
        orm_mode = True

# Схема для шаринга файлов
class ShareBase(BaseModel):
    file_id: int
    link: str

class ShareCreate(ShareBase):
    pass

class ShareOut(ShareBase):
    id: int
    class Config:
        orm_mode = True
