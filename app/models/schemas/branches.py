from app.models.schemas.base import BaseSchemaModel

class BranchIn(BaseSchemaModel):
    name: str
    address: str

class BranchOut(BaseSchemaModel):
    id: int
    name: str
    address: str
