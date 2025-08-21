from src.domain.entities.brand import Brand
from src.domain.repositories.brand_repository import BrandRepository
from uuid import UUID
from typing import Optional

class BrandRepositoryImpl(BrandRepository):
    def __init__(self):
        self.brands: list[Brand] = []

    def create_brand(self, brand: Brand) -> Brand:
        self.brands.append(brand)
        return brand

    def update_brand(self, id: UUID, brand: Brand) -> None:
        for i, existing_brand in enumerate(self.brands):
            if existing_brand.get_id == id:
                self.brands[i] = brand

    def delete_brand(self, id: UUID) -> None:
        for brand in self.brands:
            if brand.get_id == id:
                self.brands.remove(brand)

    def get_brands(self) -> list[Brand]:
        return self.brands
    
    def get_brand_by_name(self, name) -> Optional[Brand]:
        return next((b for b in self.brands if b.get_name.lower() == name.lower()), None)
    
    def get_brand_by_id(self, id: UUID) -> Optional[Brand]:
        return next((b for b in self.brands if b.get_id == id), None)