from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(100))
    desc: Mapped[str] = mapped_column(String(500))
    price: Mapped[float]
