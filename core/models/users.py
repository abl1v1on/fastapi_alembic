from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .posts import Post
    from .profiles import Profile


class User(Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(30), unique=True)

    posts: Mapped[list['Post']] = relationship(back_populates='user')
    profile: Mapped['Profile'] = relationship(back_populates='user')
