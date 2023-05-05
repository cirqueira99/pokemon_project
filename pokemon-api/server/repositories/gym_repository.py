from typing import List
from sqlalchemy.orm import Session

from server.schemas.gym_schema import GymResponse, GymRequest
from server.sqlalchemy.models.gym_model import GymModel


class GymRepository:

    @staticmethod
    def create(gym_request: GymRequest, db: Session) -> GymResponse:
        gym: GymResponse = GymModel(**gym_request.dict())

        db.add(gym)
        db.commit()
        db.refresh(gym)

        return gym

    @staticmethod
    def find_all(db: Session) -> List[GymResponse]:
        gym_list = db.query(GymModel).all()

        return gym_list

    @staticmethod
    def find_by_id(id: int, db: Session) -> GymResponse:
        gym_resp: GymResponse = db.query(GymModel).filter(GymModel.id == id).first()

        return gym_resp

    @staticmethod
    def uptade(id: int, gym_request: GymRequest, db: Session) -> GymResponse:
        gym: GymResponse = GymModel(id=id, **gym_request.dict())

        db.merge(gym)
        db.commit()

        return gym

    @staticmethod
    def delete_by_id(id: int, db: Session) -> GymResponse:
        gym: GymResponse = db.query(GymModel).filter(GymModel.id == id).first()

        if gym is not None:
            db.delete(gym)
            db.commit()

        return gym
