from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .users import User


class Post(UserRelationMixin, Base):
    __tablename__ = 'posts'
    _user_back_pupulates = 'posts'

    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(Text(), default='', server_default='')
