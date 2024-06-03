from typing import TYPE_CHECKING
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .users import User


class Profile(UserRelationMixin, Base):
    __tablename__ = 'profiles'
    _user_id_unique = True
    _user_back_pupulates = 'profile'

    first_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    bio: Mapped[str | None]

