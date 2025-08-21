from src.domain.repositories.brand_repository import BrandRepository
from uuid import UUID

class GetById:
    def __init__(self, brand_repository: BrandRepository):
        self.brand_repository = brand_repository

    def execute(self, id: UUID):
        brand = self.brand_repository.get_brand_by_id(id)

        if not brand:
            raise ValueError('Brand not found with provided id')
        
        return brand