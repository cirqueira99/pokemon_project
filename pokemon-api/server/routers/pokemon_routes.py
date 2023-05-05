from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from server.sqlalchemy.config.database import get_db
from server.repositories.pokemon_repository import PokemonRepository
from server.schemas.pokemon_schema import PokemonRequest, PokemonResponse


router_pokemon = APIRouter(prefix='/api/pokemon')


@router_pokemon.post('/create', response_model=PokemonResponse)
def create(pokemon_request: PokemonRequest, db: Session = Depends(get_db)) -> PokemonResponse:
    pokemon = PokemonRepository.create(pokemon_request, db)

    return pokemon


@router_pokemon.get('/list', response_model=List[PokemonResponse])
def find_all(db: Session = Depends(get_db)) -> List[PokemonResponse]:

    pokemon_list: List[PokemonResponse] = PokemonRepository.find_all(db)

    return pokemon_list


@router_pokemon.get("/{id}", response_model=PokemonResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    pokemon: PokemonResponse = PokemonRepository.find_by_id(id, db)

    if not pokemon:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='pokemon não encontrado!'
        )
    return PokemonResponse.from_orm(pokemon)


@router_pokemon.put("/{id}", response_model=PokemonResponse)
def update(id: int, pokemon_request: PokemonRequest, db: Session = Depends(get_db)):

    if not PokemonRepository.find_by_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="pokemon não encontrado"
        )

    pokemon = PokemonRepository.uptade(id, pokemon_request, db)

    return PokemonResponse.from_orm(pokemon)


@router_pokemon.delete("/{id}", response_model=PokemonResponse)
def delete_by_id(id: int, db: Session = Depends(get_db)):

    if not PokemonRepository.find_by_id(id, db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='pokemon não encontrado!'
        )

    pokemon: PokemonResponse = PokemonRepository.delete_by_id(id, db)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
