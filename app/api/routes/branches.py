from typing import List

from fastapi import APIRouter, Depends
from app.services.branches import BranchService
from app.models.schemas.branches import BranchOut, BranchIn
from app.core.dependencies import get_branch_service

router = APIRouter(prefix="/branches", tags=["branches"])

@router.get("/", response_model=List[BranchOut])
async def get_branches(service: BranchService = Depends(get_branch_service)):
    """
    Get all branches
    """
    return await service.get_branches()

@router.get("/{branch_id}", response_model=BranchOut)
async def get_branch_by_id(branch_id: int, service: BranchService = Depends(get_branch_service)):
    """
    Get branch by id
    """
    return await service.get_branch_by_id(branch_id)

@router.post("/", response_model=BranchOut)
async def create_branch(branch: BranchIn, service: BranchService = Depends(get_branch_service)):
    """
    Create a new branch
    """
    return await service.create_branch(branch)

@router.put("/{branch_id}", response_model=BranchOut)
async def update_branch(branch_id: int, branch: BranchIn, service: BranchService = Depends(get_branch_service)):
    """
    Update a branch
    """
    return await service.update_branch(branch_id, branch)

@router.delete("/{branch_id}")
async def delete_branch(branch_id: int, service: BranchService = Depends(get_branch_service)):
    """
    Delete a branch
    """
    return await service.delete_branch(branch_id)