

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///test.db", echo=False)

session_conn = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass
