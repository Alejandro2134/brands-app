from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class BrandCreateDTO(BaseModel):
    name: str
    owner: str

class BrandResponseDTO(BaseModel):
    id: UUID
    name: str
    owner: str
    status: bool

class BrandUpdateDTO(BaseModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    status: Optional[bool] = None