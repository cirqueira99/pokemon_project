from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
from server.sqlalchemy.config.database import Base, engine
from server.sqlalchemy.models.trainer_model import TrainerModel


class PokemonModel(Base):
    __tablename__ = "tb_pokemon"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    powers = Column(ARRAY(String), nullable=False)
    type = Column(ARRAY(String), nullable=False)
    weaknesses = Column(ARRAY(String), nullable=False)

    fk_trainer = Column(ForeignKey(TrainerModel.id), nullable=False)

    class Config:
        orm_mode = True


