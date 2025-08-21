from src.domain.repositories.brand_repository import BrandRepository
from uuid import UUID
from src.application.use_cases.brands.get_by_id import GetById

class DeleteBrand:
    def __init__(self, brand_repository: BrandRepository):
        self.brand_repository = brand_repository
        self.get_by_id = GetById(brand_repository)

    def execute(self, id: UUID):
        self.get_by_id.execute(id)
        self.brand_repository.delete_brand(id)

        

