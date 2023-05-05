from pydantic import BaseModel
from typing import List



class TrainerBase(BaseModel):
    name: str
    insignias: List[str]
    leader_gym: bool
    qt_pokemons: int
    password: str


class TrainerRequest(TrainerBase):
    ...


class TrainerResponse(TrainerBase):
    id: int

    class Config:
        orm_mode = True
