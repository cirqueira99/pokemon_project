from sqlalchemy import Column, Integer, String, ForeignKey
from server.sqlalchemy.config.database import Base
from server.sqlalchemy.models.trainer_model import TrainerModel


class GymModel(Base):
    __tablename__ = "td_gym"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    insignia = Column(String(20), nullable=False)

    fk_leader = Column(ForeignKey(TrainerModel.id), nullable=True)

    class Config:
        orm_mode = True