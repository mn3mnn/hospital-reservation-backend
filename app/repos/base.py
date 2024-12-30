from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

class BaseRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, model, entity_id: int):
        stmt = select(model).where(model.id == entity_id)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def delete_by_id(self, model, entity_id: int) -> bool:
        stmt = delete(model).where(model.id == entity_id)
        await self.db.execute(stmt)
        await self.db.commit()
        return True