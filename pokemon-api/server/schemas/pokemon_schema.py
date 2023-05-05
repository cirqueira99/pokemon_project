from pydantic import BaseModel
from typing import List


class PokemonBase(BaseModel):
    name: str
    fk_trainer: int
    powers: str
    weaknesses: List[str]
    type: str


class PokemonRequest(PokemonBase):
    ...


class PokemonResponse(PokemonBase):
    id: int

    class Config:
        orm_mode = True
