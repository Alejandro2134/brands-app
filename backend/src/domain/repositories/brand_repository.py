from typing import Optional
from uuid import UUID
from src.domain.entities.brand import Brand
from abc import ABCMeta, abstractmethod

class BrandRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_brand(self, brand: Brand) -> Brand:
        pass

    @abstractmethod 
    def get_brands(self) -> list[Brand]:
        pass

    @abstractmethod
    def update_brand(self, id: UUID, brand: Brand) -> None:
        pass

    @abstractmethod
    def delete_brand(self, id: UUID) -> None:
        pass

    @abstractmethod
    def get_brand_by_name(self, name: str) -> Optional[Brand]:
        pass

    @abstractmethod
    def get_brand_by_id(self, id: UUID) -> Optional[Brand]:
        pass