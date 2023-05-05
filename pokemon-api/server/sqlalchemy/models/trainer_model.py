from server.sqlalchemy.config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ARRAY
from typing import List


class TrainerModel(Base):
    __tablename__ = "tb_trainer"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    insignias: List[str] = Column(ARRAY(String), nullable=True)
    leader_gym: bool = Column(Boolean, nullable=False)
    qt_pokemons: int = Column(Integer, nullable=False, default=0)
    password: str = Column(String, nullable=False)

