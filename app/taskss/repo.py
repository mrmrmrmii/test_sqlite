from app.database import session_conn
from app.taskss.model import tasks
from sqlalchemy import select, insert, delete, update

class DAO:
    model = tasks

    @classmethod
    async def get_all(cls):
        async with session_conn() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_by_id(cls, id: int):
        async with session_conn() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)
            return result.scalar_one_or_none()


    @classmethod
    async def add(cls, **data):
        async with session_conn() as session:
            query = insert(cls.model).values(**data).returning(cls.model.id)
            result = await session.execute(query)
            await session.commit()
            return result.mappings().one()


    @classmethod
    async def delete_one(cls, id):
        async with session_conn() as session:
            query = delete(cls.model).where(cls.model.id == id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_task(cls, id, **data):
        async with session_conn() as session:
            query = update(cls.model).where(cls.model.id == id).values(**data)
            await session.execute(query)
            await session.commit()
            query1 = await session.get(cls.model, id)
            return query1
