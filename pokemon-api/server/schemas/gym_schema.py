from pydantic import BaseModel


class GymBase(BaseModel):
    id: int
    name: str
    insignia: str
    fk_leader: int


class GymRequest(GymBase):
    ...


class GymResponse(GymBase):
    id: int

    class Config:
        orm_mode = True
