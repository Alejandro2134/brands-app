from uuid import uuid4, UUID

class Brand:
    def __init__(self, name: str, owner: str, status: bool = True, id: UUID = None):
        self.__id = id or uuid4()
        self.__name = name
        self.__owner = owner
        self.__status = status

    @property
    def get_name(self) -> str:
        return self.__name
    
    @property
    def get_owner(self) -> str:
        return self.__owner
    
    @property
    def get_status(self) -> bool:
        return self.__status
    
    @property
    def get_id(self) -> UUID:
        return self.__id
    
    @get_name.setter
    def set_name(self, name: str):
        self.__name = name

    @get_owner.setter
    def set_owner(self, owner: str):
        self.__owner = owner

    @get_status.setter
    def set_status(self, status: bool):
        self.__status = status
    
class BrandUpdate:
    def __init__(self, name: str = None, owner: str = None, status: bool = None):
        self.name = name
        self.owner = owner
        self.status = status