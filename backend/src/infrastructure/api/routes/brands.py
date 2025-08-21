from src.application.use_cases.brands.create import CreateBrand
from src.infrastructure.persistency.memory.repositories.brand_repository_impl import BrandRepositoryImpl
from src.domain.repositories.brand_repository import BrandRepository
from fastapi import HTTPException, APIRouter
from src.application.dto.brand import BrandCreateDTO, BrandResponseDTO, BrandUpdateDTO
from src.application.mappers.brands.mapper import BrandMapper
from src.application.use_cases.brands.get import GetBrands
from src.application.use_cases.brands.delete import DeleteBrand
from src.application.use_cases.brands.update import UpdateBrand
from uuid import UUID

brand_repository: BrandRepository = BrandRepositoryImpl()
router = APIRouter()
brand_mapper: BrandMapper = BrandMapper()

@router.post('/', status_code=201, response_model=BrandResponseDTO)
def create_brand(dto: BrandCreateDTO):
    use_case = CreateBrand(brand_repository)

    try:
        brand_entity = brand_mapper.from_dto_create_to_entity(dto)
        brand = use_case.execute(brand_entity)
        return brand_mapper.from_entity_to_dto(brand)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get('/', response_model=list[BrandResponseDTO], status_code=200)
def get_brands():
    use_case = GetBrands(brand_repository)

    try:
        brands = use_case.execute()
        return [brand_mapper.from_entity_to_dto(brand) for brand in brands]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete('/{id}', status_code=204)
def delete_brand(id: str):
    use_case = DeleteBrand(brand_repository)

    try:
        use_case.execute(UUID(id))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.put('/{id}', response_model=BrandResponseDTO, status_code=200)
def update_brand(id: str, dto: BrandUpdateDTO):
    use_case = UpdateBrand(brand_repository)

    try:
        brand_update_entity = brand_mapper.from_dto_update_to_entity(dto)
        updated_brand = use_case.execute(UUID(id), brand_update_entity)
        return brand_mapper.from_entity_to_dto(updated_brand)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))