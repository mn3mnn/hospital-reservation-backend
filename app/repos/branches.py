from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.db.branches import Branch
from app.models.schemas.branches import BranchIn, BranchOut
from app.repos.base import BaseRepository
from typing import List, Optional

class BranchRepository(BaseRepository):
    async def get_branches(self) -> List[BranchOut]:
        stmt = select(Branch)
        result = await self.db.execute(stmt)
        branches = result.scalars().all()
        return [BranchOut.model_validate(branch) for branch in branches]

    async def get_branch_by_id(self, branch_id: int) -> Optional[BranchOut]:
        branch = await self.get_by_id(Branch, branch_id)
        if branch:
            return BranchOut.model_validate(branch)
        return None

    async def create_branch(self, branch: BranchIn) -> Branch:
        branch_db = Branch(**branch.model_dump())
        self.db.add(branch_db)
        await self.db.commit()
        await self.db.refresh(branch_db)
        return branch_db

    async def update_branch(self, branch_id: int, branch: BranchIn) -> BranchOut:
        branch_db = await self.get_by_id(Branch, branch_id)
        if not branch_db:
            return None

        for field, value in branch.model_dump().items():
            setattr(branch_db, field, value)

        await self.db.commit()
        await self.db.refresh(branch_db)
        return BranchOut.model_validate(branch_db)

    async def delete_branch(self, branch_id: int) -> bool:
        return await self.delete_by_id(Branch, branch_id)
