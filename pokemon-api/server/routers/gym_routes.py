from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from server.sqlalchemy.config.database import get_db
from server.repositories.gym_repository import GymRepository
from server.schemas.gym_schema import GymRequest, GymResponse


router_gym = APIRouter(prefix='/api/gym')


@router_gym.post('/create', response_model=GymResponse)
def create(gym_request: GymRequest, db: Session = Depends(get_db)) -> GymResponse:
    gym = GymRepository.create(gym_request, db)

    return gym


@router_gym.get('/list', response_model=List[GymResponse])
def find_all(db: Session = Depends(get_db)) -> List[GymResponse]:

    gym_list: List[GymResponse] = GymRepository.find_all(db)

    return gym_list


@router_gym.get("/{id}", response_model=GymResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    gym: GymResponse = GymRepository.find_by_id(id, db)

    if not gym:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Gym não encontrado!'
        )
    return GymResponse.from_orm(gym)


@router_gym.put("/{id}", response_model=GymResponse)
def update(id: int, gym_request: GymRequest, db: Session = Depends(get_db)):

    if not GymRepository.find_by_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Gym não encontrado"
        )

    gym = GymRepository.uptade(id, gym_request, db)

    return GymResponse.from_orm(gym)


@router_gym.delete("/{id}", response_model=GymResponse)
def delete_by_id(id: int, db: Session = Depends(get_db)):

    if not GymRepository.find_by_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Gym não encontrado!'
        )

    gym: GymResponse = GymRepository.delete_by_id(id, db)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
