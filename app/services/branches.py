from typing import List
from app.models.schemas.branches import BranchIn, BranchOut
from app.repos.branches import BranchRepository

class BranchService:
    def __init__(self, repo: BranchRepository):
        self.repo = repo

    async def get_branches(self) -> List[BranchOut]:
        return await self.repo.get_branches()

    async def get_branch_by_id(self, branch_id: int) -> BranchOut:
        return await self.repo.get_branch_by_id(branch_id)

    async def create_branch(self, branch: BranchIn) -> BranchOut:
        branch_db = await self.repo.create_branch(branch)
        return BranchOut(**branch_db.__dict__)

    async def update_branch(self, branch_id: int, branch: BranchIn) -> BranchOut:
        return await self.repo.update_branch(branch_id, branch)

    async def delete_branch(self, branch_id: int) -> None:
        await self.repo.delete_branch(branch_id)
