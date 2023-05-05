from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from server.sqlalchemy.config.database import get_db
from server.repositories.trainer_repository import TrainerRepository
from server.schemas.trainer_schema import TrainerRequest, TrainerResponse


router_trainer = APIRouter(prefix='/api/trainer')


@router_trainer.post('/create', response_model=TrainerResponse)
def create(trainer_request: TrainerRequest, db: Session = Depends(get_db)) -> TrainerResponse:
    trainer = TrainerRepository.create(trainer_request, db)

    return trainer


@router_trainer.get('/list', response_model=List[TrainerResponse])
def find_all(db: Session = Depends(get_db)) -> List[TrainerResponse]:

    trainer_list: List[TrainerResponse] = TrainerRepository.find_all(db)

    return trainer_list


@router_trainer.get("/{id}", response_model=TrainerResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    trainer: TrainerResponse = TrainerRepository.find_by_id(id, db)

    if not trainer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Trainer não encontrado!'
        )
    return TrainerResponse.from_orm(trainer)


@router_trainer.put("/{id}", response_model=TrainerResponse)
def update(id: int, trainer_request: TrainerRequest, db: Session = Depends(get_db)):

    if not TrainerRepository.find_by_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Trainer não encontrado"
        )

    trainer = TrainerRepository.uptade(id, trainer_request, db)

    return TrainerResponse.from_orm(trainer)


@router_trainer.delete("/{id}", response_model=TrainerResponse)
def delete_by_id(id: int, db: Session = Depends(get_db)):

    if not TrainerRepository.find_by_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Trainer não encontrado!'
        )

    trainer: TrainerResponse = TrainerRepository.delete_by_id(id, db)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
