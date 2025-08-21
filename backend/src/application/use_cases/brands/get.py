from src.domain.repositories.brand_repository import BrandRepository

class GetBrands:
    def __init__(self, brand_repository: BrandRepository):
        self.brand_repository = brand_repository

    def execute(self):
        return self.brand_repository.get_brands()