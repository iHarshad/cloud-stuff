from datetime import datetime
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(init=False, autoincrement=True, primary_key=True)
    name: Mapped[str]
    email: Mapped[Optional[str]]
    # created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.current_timestamp()
    )

    def __str__(self):
        return f"From str method of User: ID = {self.id} \nName = {self.name} \nEmail = {self.email} \nCreated at = {self.created_at}\n"
