from src.domain.repositories.brand_repository import BrandRepository
from src.domain.entities.brand import Brand, BrandUpdate
from src.application.use_cases.brands.get_by_name import GetByName
from src.application.use_cases.brands.get_by_id import GetById
from uuid import UUID

class UpdateBrand:
    def __init__(self, brand_repository: BrandRepository):
        self.brand_repository = brand_repository
        self.get_by_name = GetByName(brand_repository)
        self.get_by_id = GetById(brand_repository)

    def execute(self, id: UUID, brand: BrandUpdate):
        found_brand = self.get_by_id.execute(id)

        if brand.name is not None:
            existing_brand = self.get_by_name.execute(brand.name)
            if existing_brand:
                raise ValueError('Brand with that name already exists')
            found_brand.set_name = brand.name
            
        if brand.owner is not None:
            found_brand.set_owner = brand.owner

        if brand.status is not None:
            found_brand.set_status = brand.status

        self.brand_repository.update_brand(id, found_brand)

        return found_brand