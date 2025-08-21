from src.domain.repositories.brand_repository import BrandRepository
from src.domain.entities.brand import Brand
from src.application.use_cases.brands.get_by_name import GetByName

class CreateBrand:
    def __init__(self, brand_repository: BrandRepository):
        self.brand_repository = brand_repository
        self.get_by_name = GetByName(brand_repository)

    def execute(self, brand: Brand):
       existing_brand = self.get_by_name.execute(brand.get_name)

       if existing_brand:
            raise ValueError('Brand with that name already exists')

       return self.brand_repository.create_brand(brand)