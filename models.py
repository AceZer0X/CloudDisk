# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base


# Модель пользователя
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)


# Модель файла
class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content_type = Column(String)
    path = Column(String)  # Путь к файлу
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="files")


# Модель папки
class Folder(Base):
    __tablename__ = 'folders'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    parent_id = Column(Integer, ForeignKey('folders.id'), nullable=True)  # Для вложенных папок
    owner_id = Column(Integer, ForeignKey('users.id'))

    parent = relationship("Folder", remote_side=[id], back_populates="subfolders")
    subfolders = relationship("Folder", back_populates="parent")
    files = relationship("File", back_populates="folder")

    owner = relationship("User", back_populates="folders")


# Модель шаринга
class Share(Base):
    __tablename__ = 'shares'

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(Integer, ForeignKey('files.id'))
    link = Column(String, unique=True)

    file = relationship("File", back_populates="shares")
