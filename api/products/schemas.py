from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    desc: str
    price: float


class ProductCreate(BaseModel):
    name: str
    desc: str
    price: float
