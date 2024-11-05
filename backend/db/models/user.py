from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped

from .. import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str]
    email: Mapped[str]
    hashed_password: Mapped[str]
