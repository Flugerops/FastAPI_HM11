from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class AsyncDB:
    ENGINE = create_engine("sqlite:///users.db")
    SESSION = sessionmaker(bind=ENGINE)

    @classmethod
    def up(cls):
        Base.metadata.create_all(cls.ENGINE)

    @classmethod
    def down(cls):
        Base.metadata.drop_all(cls.ENGINE)

    @classmethod
    def migrate(cls):
        Base.metadata.drop_all(cls.ENGINE)
        Base.metadata.create_all(cls.ENGINE)

    @classmethod
    def get_session(cls):
        with cls.SESSION.begin() as session:
            yield session

    @classmethod
    def create_mock_data(cls, hash_func):
        with cls.SESSION.begin() as session:
            mock_user1 = User(
                username="John Doe",
                email="JohnDoe@gmail.com",
                hashed_password=hash_func("test1"),
            )
            mock_user2 = User(
                username="Dmytro",
                email="Test@gmail.com",
                hashed_password=hash_func("test2"),
            )
            session.add(mock_user1, mock_user2)


from .models import User
