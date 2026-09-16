from sqlalchemy import Column, Integer, String, Numeric, Date, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "auth_users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False, default="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    entry_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("auth_users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    purchase_date = Column(DateTime, nullable=False, server_default=func.now())