from sqlalchemy import Column, Integer, String, DateTime, CHAR, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer(), primary_key=True)
    number = Column(Integer(), nullable=False)
    symbol = Column(CHAR(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(), nullable=True, onupdate=datetime.now)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer(), primary_key=True)
    full_name = Column(String(), nullable=False)
    group_id = Column(Integer(), ForeignKey('groups.id'))
    phone_number = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    telegram_id = Column(String(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(), nullable=True, onupdate=datetime.now)


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer(), primary_key=True)
    code = Column(String(), unique=True, nullable=False)
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(), nullable=True, onupdate=datetime.now)


class History(Base):
    __tablename__ = "histories"

    id = Column(Integer(), primary_key=True)
    notified_at = Column(DateTime(), nullable=True)
    created_at = Column(DateTime(), default=datetime.now, nullable=False)
    updated_at = Column(DateTime(), nullable=True, onupdate=datetime.now)
