from typing import List
from sqlalchemy.orm import Session

from server.schemas.trainer_schema import TrainerResponse, TrainerRequest
from server.sqlalchemy.models.trainer_model import TrainerModel


class TrainerRepository:

    @staticmethod
    def create(trainer_request: TrainerRequest, db: Session) -> TrainerResponse:
        trainer: TrainerResponse = TrainerModel(**trainer_request.dict())

        db.add(trainer)
        db.commit()
        db.refresh(trainer)

        return trainer

    @staticmethod
    def find_all(db: Session) -> List[TrainerResponse]:

        trainer_list = db.query(TrainerModel).all()

        return trainer_list

    @staticmethod
    def find_by_id(id: int, db: Session) -> TrainerResponse:
        trainer_resp: TrainerResponse = db.query(TrainerModel).filter(TrainerModel.id == id).first()

        return trainer_resp

    @staticmethod
    def uptade(id: int, trainer_request: TrainerRequest, db: Session) -> TrainerResponse:
        trainer: TrainerResponse = TrainerModel(id= id, **trainer_request.dict())

        db.merge(trainer)
        db.commit()

        return trainer

    @staticmethod
    def delete_by_id(id: int, db: Session) -> TrainerResponse:
        trainer: TrainerResponse = db.query(TrainerModel).filter(TrainerModel.id == id).first()

        if trainer is not None:
            db.delete(trainer)
            db.commit()

        return trainer
