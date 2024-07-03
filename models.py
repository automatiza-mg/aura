from pathlib import Path
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
)
from typing import (
    List,
    Optional,
)

engine = create_engine("sqlite+pysqlite:///database.db", echo=True)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
     __tablename__ = 'users'

     name: Mapped[str] = mapped_column(String(30))
     fullname: Mapped[Optional[str]]

     addresses: Mapped[List['Address']] = relationship(back_populates='user')

     def __repr__(self) -> str:
         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "addresses"

    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("users.id"))
    user: Mapped[User] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

if not Path('databese.db').exists():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    sandy = User(name="sandy", fullname="Sandy Cheeks")
    address = Address(email_address='sandy@teste.com', user=sandy)
    session.add(sandy)
    session.add(address)
    session.commit()
    session.close()

Session = sessionmaker(bind=engine)
session = Session()
first_user = session.query(User).first()
