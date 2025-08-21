from src.domain.entities.brand import Brand, BrandUpdate
from src.application.dto.brand import BrandResponseDTO, BrandCreateDTO, BrandUpdateDTO

class BrandMapper:
    def from_entity_to_dto(self, entity: Brand):
        return BrandResponseDTO(
            id=entity.get_id,
            name=entity.get_name,
            owner=entity.get_owner,
            status=entity.get_status,
        )
    
    def from_dto_create_to_entity(self, dto: BrandCreateDTO):
        return Brand(
            name=dto.name,
            owner=dto.owner,
        )
    
    def from_dto_update_to_entity(self, dto: BrandUpdateDTO):
        return BrandUpdate(
            name=dto.name,
            owner=dto.owner,
            status=dto.status,
        )