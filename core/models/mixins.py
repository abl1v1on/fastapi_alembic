from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .users import User


class UserRelationMixin:
    _user_id_unique: bool = False
    _user_back_pupulates: str | None = None

    @declared_attr
    def user_id(self) -> Mapped[int]:
        return mapped_column(ForeignKey('users.id'), unique=self._user_id_unique)
    

    @declared_attr
    def user(self) -> Mapped['User']:
        return relationship('User', back_populates=self._user_back_pupulates)
