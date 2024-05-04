# from datetime import datetime
# from typing import Optional
#
# from sqlalchemy import func
# from sqlalchemy.orm import Mapped, mapped_column
#
# from .base import Base
#
#
# class Message(Base):
#     __tablename__ = "users"
#
#     id: Mapped[int] = mapped_column(init=False, autoincrement=True, primary_key=True)
#     text_msg: Mapped[Optional[str]]
#     created_at: Mapped[datetime] = mapped_column(
#         init=False, server_default=func.current_timestamp()
#     )
